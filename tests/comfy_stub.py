"""A minimal stand-in for the parts of ComfyUI the nodes import, so tests run without ComfyUI.

It records what the nodes declare (inputs, outputs, defaults) instead of drawing anything, and
checks the same things ComfyUI checks when it loads a node: every input has a unique name, a
combo default is one of its options, and numbers sit inside their range.
"""

from __future__ import annotations

import atexit
import shutil
import sys
import tempfile
import types
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Input:
    socket: str
    name: str
    options: dict[str, Any] = field(default_factory=dict)

    @property
    def optional(self) -> bool:
        return bool(self.options.get("optional"))


@dataclass
class Output:
    socket: str
    name: str
    options: dict[str, Any] = field(default_factory=dict)


def _socket(kind: str) -> Any:
    class Socket:
        type_name = kind

        @staticmethod
        def Input(name: str, **options: Any) -> Input:  # noqa: N802 - mirrors ComfyUI's API
            if kind == "COMBO":
                assert options.get("default") in options["options"], (name, options)
            if kind in ("INT", "FLOAT") and options.get("default") is not None:
                assert options["min"] <= options["default"] <= options["max"], (name, options)
            return Input(kind, name, options)

        @staticmethod
        def Output(name: str, **options: Any) -> Output:  # noqa: N802
            return Output(kind, name, options)

    return Socket


class Schema:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)
        names = [i.name for i in kwargs.get("inputs", [])]
        assert len(names) == len(set(names)), f"duplicate input names in {kwargs.get('node_id')}"


class ComfyNode:
    hidden = None

    @classmethod
    def GET_SCHEMA(cls) -> Schema:  # noqa: N802
        return cls.define_schema()


class NodeOutput(tuple):
    def __new__(cls, *values: Any) -> NodeOutput:
        return super().__new__(cls, values)


class Autogrow:
    @staticmethod
    def TemplatePrefix(socket: Input, **options: Any) -> dict[str, Any]:  # noqa: N802
        return {"socket": socket, **options}

    @staticmethod
    def Input(name: str, **options: Any) -> Input:  # noqa: N802
        return Input("AUTOGROW", name, options)


def Custom(name: str) -> Any:  # noqa: N802
    return _socket(name)


def install() -> types.SimpleNamespace:
    """Register the fake modules; returns the fake ``io`` namespace."""
    io = types.SimpleNamespace(
        ComfyNode=ComfyNode,
        Schema=Schema,
        NodeOutput=NodeOutput,
        Autogrow=Autogrow,
        Custom=Custom,
        Image=_socket("IMAGE"),
        Video=_socket("VIDEO"),
        Audio=_socket("AUDIO"),
        Mask=_socket("MASK"),
        String=_socket("STRING"),
        Int=_socket("INT"),
        Float=_socket("FLOAT"),
        Boolean=_socket("BOOLEAN"),
        Combo=_socket("COMBO"),
        Hidden=types.SimpleNamespace(unique_id="UNIQUE_ID"),
        ControlAfterGenerate=types.SimpleNamespace(fixed="fixed", randomize="randomize"),
        NumberDisplay=types.SimpleNamespace(slider="slider", number="number"),
        Input=Input,
        Output=Output,
    )

    class ComfyExtension:
        pass

    latest = types.ModuleType("comfy_api.latest")
    latest.io = io
    latest.ComfyExtension = ComfyExtension
    comfy_api = types.ModuleType("comfy_api")
    comfy_api.latest = latest
    sys.modules.setdefault("comfy_api", comfy_api)
    sys.modules.setdefault("comfy_api.latest", latest)

    management = types.ModuleType("comfy.model_management")
    management.throw_exception_if_processing_interrupted = lambda: None
    comfy = types.ModuleType("comfy")
    comfy.model_management = management
    sys.modules.setdefault("comfy", comfy)
    sys.modules.setdefault("comfy.model_management", management)

    if "folder_paths" in sys.modules:
        return sys.modules["comfy_api.latest"].io
    folder_paths = types.ModuleType("folder_paths")
    scratch = tempfile.mkdtemp(prefix="popnow-comfy-test-")
    atexit.register(shutil.rmtree, scratch, True)
    folder_paths.get_output_directory = lambda: scratch
    folder_paths.get_input_directory = lambda: scratch
    folder_paths.get_user_directory = lambda: scratch
    folder_paths.get_full_path = lambda _kind, _name: None
    folder_paths.scratch = scratch
    sys.modules["folder_paths"] = folder_paths
    return sys.modules["comfy_api.latest"].io
