from typing import cast

from ape.api.config import PluginConfig
from ape_ethereum.ecosystem import Ethereum, NetworkConfig, create_network_config

NETWORKS = {
    # chain_id, network_id
    "opera": (250, 250),
    "testnet": (4002, 4002),
}


class FantomConfig(PluginConfig):
    opera: NetworkConfig = create_network_config(block_time=0, required_confirmations=0)
    testnet: NetworkConfig = create_network_config(block_time=0, required_confirmations=0)


class Fantom(Ethereum):
    @property
    def config(self) -> FantomConfig:  # type: ignore[override]
        return cast(FantomConfig, self.config_manager.get_config("fantom"))
