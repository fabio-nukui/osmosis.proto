.PHONY: all update-deps install proto-pull proto-gen format

################################################################################################
## VARIABLES
################################################################################################

OSMOSIS_VERSION ?= v4.2.0
COSMOS_SDK_VERSION ?= v0.42.9

################################################################################################
## GENERAL COMMANDS
################################################################################################

all: install proto-pull proto-gen build

update-deps:
	@echo "Updating dependencies"
	poetry update

install:
	@echo "Installing dependencies"
	poetry install

proto-pull:
	@echo "Pull external .proto files"
	git submodule update --init --recursive
	(cd ../osmosis && git fetch && git checkout ${OSMOSIS_VERSION})
	(cd ../cosmos-sdk && git fetch && git checkout ${COSMOS_SDK_VERSION})

proto-gen:
	@echo "Generating Protobuf files"
	./scripts/proto-gen.sh

build:
	@echo "Building distribution artifacts"
	poetry build
