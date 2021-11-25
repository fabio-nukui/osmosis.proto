# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/upgrade/v1beta1/query.proto, cosmos/upgrade/v1beta1/upgrade.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class Plan(betterproto.Message):
    """
    Plan specifies information about a planned upgrade and when it should
    occur.
    """

    # Sets the name for the upgrade. This name will be used by the upgraded
    # version of the software to apply any special "on-upgrade" commands during
    # the first BeginBlock method after the upgrade is applied. It is also used
    # to detect whether a software version can handle a given upgrade. If no
    # upgrade handler with this name has been set in the software, it will be
    # assumed that the software is out-of-date when the upgrade Time or Height is
    # reached and the software will exit.
    name: str = betterproto.string_field(1)
    # The time after which the upgrade must be performed. Leave set to its zero
    # value to use a pre-defined Height instead.
    time: datetime = betterproto.message_field(2)
    # The height at which the upgrade must be performed. Only used if Time is not
    # set.
    height: int = betterproto.int64_field(3)
    # Any application specific upgrade info to be included on-chain such as a git
    # commit that validators could automatically upgrade to
    info: str = betterproto.string_field(4)
    # IBC-enabled chains can opt-in to including the upgraded client state in its
    # upgrade plan This will make the chain commit to the correct upgraded (self)
    # client state before the upgrade occurs, so that connecting chains can
    # verify that the new upgraded client is valid by verifying a proof on the
    # previous version of the chain. This will allow IBC connections to persist
    # smoothly across planned chain upgrades
    upgraded_client_state: "betterproto_lib_google_protobuf.Any" = (
        betterproto.message_field(5)
    )


@dataclass(eq=False, repr=False)
class SoftwareUpgradeProposal(betterproto.Message):
    """
    SoftwareUpgradeProposal is a gov Content type for initiating a software
    upgrade.
    """

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    plan: "Plan" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CancelSoftwareUpgradeProposal(betterproto.Message):
    """
    CancelSoftwareUpgradeProposal is a gov Content type for cancelling a
    software upgrade.
    """

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class QueryCurrentPlanRequest(betterproto.Message):
    """
    QueryCurrentPlanRequest is the request type for the Query/CurrentPlan RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryCurrentPlanResponse(betterproto.Message):
    """
    QueryCurrentPlanResponse is the response type for the Query/CurrentPlan RPC
    method.
    """

    # plan is the current upgrade plan.
    plan: "Plan" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAppliedPlanRequest(betterproto.Message):
    """
    QueryCurrentPlanRequest is the request type for the Query/AppliedPlan RPC
    method.
    """

    # name is the name of the applied plan to query for.
    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryAppliedPlanResponse(betterproto.Message):
    """
    QueryAppliedPlanResponse is the response type for the Query/AppliedPlan RPC
    method.
    """

    # height is the block height at which the plan was applied.
    height: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class QueryUpgradedConsensusStateRequest(betterproto.Message):
    """
    QueryUpgradedConsensusStateRequest is the request type for the
    Query/UpgradedConsensusState RPC method.
    """

    # last height of the current chain must be sent in request as this is the
    # height under which next consensus state is stored
    last_height: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class QueryUpgradedConsensusStateResponse(betterproto.Message):
    """
    QueryUpgradedConsensusStateResponse is the response type for the
    Query/UpgradedConsensusState RPC method.
    """

    upgraded_consensus_state: "betterproto_lib_google_protobuf.Any" = (
        betterproto.message_field(1)
    )


class QueryStub(betterproto.ServiceStub):
    async def current_plan(self) -> "QueryCurrentPlanResponse":

        request = QueryCurrentPlanRequest()

        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Query/CurrentPlan",
            request,
            QueryCurrentPlanResponse,
        )

    async def applied_plan(self, *, name: str = "") -> "QueryAppliedPlanResponse":

        request = QueryAppliedPlanRequest()
        request.name = name

        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Query/AppliedPlan",
            request,
            QueryAppliedPlanResponse,
        )

    async def upgraded_consensus_state(
        self, *, last_height: int = 0
    ) -> "QueryUpgradedConsensusStateResponse":

        request = QueryUpgradedConsensusStateRequest()
        request.last_height = last_height

        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Query/UpgradedConsensusState",
            request,
            QueryUpgradedConsensusStateResponse,
        )


class QueryBase(ServiceBase):
    async def current_plan(self) -> "QueryCurrentPlanResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def applied_plan(self, name: str) -> "QueryAppliedPlanResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upgraded_consensus_state(
        self, last_height: int
    ) -> "QueryUpgradedConsensusStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_current_plan(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.current_plan(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_applied_plan(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "name": request.name,
        }

        response = await self.applied_plan(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_upgraded_consensus_state(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "last_height": request.last_height,
        }

        response = await self.upgraded_consensus_state(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.upgrade.v1beta1.Query/CurrentPlan": grpclib.const.Handler(
                self.__rpc_current_plan,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryCurrentPlanRequest,
                QueryCurrentPlanResponse,
            ),
            "/cosmos.upgrade.v1beta1.Query/AppliedPlan": grpclib.const.Handler(
                self.__rpc_applied_plan,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAppliedPlanRequest,
                QueryAppliedPlanResponse,
            ),
            "/cosmos.upgrade.v1beta1.Query/UpgradedConsensusState": grpclib.const.Handler(
                self.__rpc_upgraded_consensus_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryUpgradedConsensusStateRequest,
                QueryUpgradedConsensusStateResponse,
            ),
        }


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf