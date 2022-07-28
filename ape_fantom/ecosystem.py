from typing import Dict

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.api.providers import BlockAPI
from ape_ethereum.ecosystem import Block as EthereumBlock
from ape_ethereum.ecosystem import Ethereum, NetworkConfig
from pydantic import validator

NETWORKS = {
    # chain_id, network_id
    "opera": (250, 250),
    "testnet": (4002, 4002),
}


class FantomConfig(PluginConfig):
    opera: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=1)  # type: ignore
    testnet: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=1)  # type: ignore
    local: NetworkConfig = NetworkConfig(default_provider="test")  # type: ignore
    default_network: str = LOCAL_NETWORK_NAME


class Block(EthereumBlock):
    timestamp_nano: int

    @validator("timestamp_nano", pre=True)
    def validate_nano_timestamp(cls, value):
        if value and not (
            isinstance(value, str)
            and value.startswith("0x")
            and set(value[2:]) < set("0123456789abcdef")
        ):
            raise ValueError(f"Hash `{value}` is not a valid hexstr.")

        return int(value, 16)


class Fantom(Ethereum):
    @property
    def config(self) -> FantomConfig:  # type: ignore
        return self.config_manager.get_config("fantom")  # type: ignore

    def decode_block(self, data: Dict) -> BlockAPI:
        block = super().decode_block(data)
        return Block(timestamp_nano=data.get("timestampNano", 0), **block.dict())
