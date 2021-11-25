import importlib

from betterproto import Message
from betterproto.lib.google.protobuf import Any as Any_pb


def from_any(proto: Any_pb) -> Message:
    if proto.type_url[0] != "/":
        raise ValueError(f"type_url must start with '/': {proto.type_url}")
    module_name, _, class_name = proto.type_url[1:].rpartition(".")
    module = importlib.import_module(f"osmosis_proto.{module_name}")
    cls: Message = getattr(module, class_name)
    return cls.FromString(proto.value)
