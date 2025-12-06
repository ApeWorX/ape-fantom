from datetime import datetime
from typing import ClassVar, cast

from ape.types import HexBytes, HexInt
from ape_ethereum.ecosystem import BaseEthereumConfig
from ape_ethereum.ecosystem import Block as EthereumBlock
from ape_ethereum.ecosystem import Ethereum, NetworkConfig, create_network_config
from pydantic import Field, model_validator

NETWORKS = {
    # chain_id, network_id
    "opera": (250, 250),
    "testnet": (4002, 4002),
}


class FantomConfig(BaseEthereumConfig):
    NETWORKS: ClassVar[dict[str, tuple[int, int]]] = NETWORKS
    opera: NetworkConfig = create_network_config(
        block_time=0, required_confirmations=0, is_mainnet=True
    )
    testnet: NetworkConfig = create_network_config(block_time=0, required_confirmations=0)


class Block(EthereumBlock):
    timestamp_nano: HexInt = Field(alias="timestampNano")

    @model_validator(mode="before")
    def validate_nano_timestamp(cls, values: dict):
        if not values.get("timestamp_nano"):
            # NOTE: For instances like using it with anvil or hardhat, which doesn't have this field
            values["timestamp_nano"] = values["timestamp"] * int(1e9)

        return values

    @property
    def datetime(self) -> datetime:
        return super().datetime.replace(microsecond=((self.timestamp_nano % int(1e9)) // int(1e3)))


class Fantom(Ethereum):
    fee_token_symbol: str = "FTM"

    @property
    def config(self) -> FantomConfig:  # type: ignore[override]
        return cast(FantomConfig, self.config_manager.get_config("fantom"))

    def decode_block(self, data: dict) -> Block:
        # NOTE: Copied from `ape_ethereum.Ethereum.decode_block`
        data["hash"] = HexBytes(data["hash"]) if data.get("hash") else None
        if "gas_limit" in data:
            data["gasLimit"] = data.pop("gas_limit")
        if "gas_used" in data:
            data["gasUsed"] = data.pop("gas_used")
        if "parent_hash" in data:
            data["parentHash"] = HexBytes(data.pop("parent_hash"))
        if "transaction_ids" in data:
            data["transactions"] = data.pop("transaction_ids")
        if "total_difficulty" in data:
            data["totalDifficulty"] = data.pop("total_difficulty") or 0
        elif "totalDifficulty" in data:
            data["totalDifficulty"] = data.pop("totalDifficulty") or 0
        if "base_fee" in data:
            data["baseFeePerGas"] = data.pop("base_fee")
        elif "baseFee" in data:
            data["baseFeePerGas"] = data.pop("baseFee")
        if "transactions" in data:
            data["num_transactions"] = len(data["transactions"])
        if "timestampNano" not in data:
            data["timestampNano"] = data["timestamp"] * int(1e9)

        return Block.model_validate(data)
