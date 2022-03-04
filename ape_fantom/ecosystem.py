from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig

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


class Fantom(Ethereum):
    @property
    def config(self) -> FantomConfig:  # type: ignore
        return self.config_manager.get_config("fantom")  # type: ignore
