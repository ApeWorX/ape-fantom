from typing import ClassVar, cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

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


class Fantom(Ethereum):
    fee_token_symbol: str = "FTM"

    @property
    def config(self) -> FantomConfig:  # type: ignore[override]
        return cast(FantomConfig, self.config_manager.get_config("fantom"))
