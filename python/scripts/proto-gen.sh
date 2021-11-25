#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck >/dev/null && shellcheck "$0"

OUT_DIR="./osmosis_proto"

mkdir -p "$OUT_DIR"

echo "Processing osmosis proto files ..."

OSMOSIS_DIR="../osmosis/proto"
COSMOS_SDK_DIR="../cosmos-sdk/proto"
COSMOS_SDK_THIRD_PARTY_DIR="../cosmos-sdk/third_party/proto"

protoc \
  --proto_path=${OSMOSIS_DIR} \
  --proto_path=${COSMOS_SDK_DIR} \
  --proto_path=${COSMOS_SDK_THIRD_PARTY_DIR} \
  --python_betterproto_out="${OUT_DIR}" \
  $(find ${OSMOSIS_DIR} ${COSMOS_SDK_DIR} -path -prune -o -name '*.proto' -print0 | xargs -0)
