# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: osmosis/gamm/v1beta1/genesis.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params holds parameters for the incentives module"""

    pool_creation_fee: List[
        "__cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the gamm module's genesis state."""

    pools: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)
    next_pool_number: int = betterproto.uint64_field(2)
    params: "Params" = betterproto.message_field(3)


from ...cosmos.base import v1beta1 as __cosmos_base_v1_beta1__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf