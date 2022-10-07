from typing import Optional

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "opera": (250, 250),
    "testnet": (4002, 4002),
}


def _create_network_config(
    required_confirmations: int = 1, block_time: int = 1, **kwargs
) -> NetworkConfig:
    # Helper method to isolate `type: ignore` comments.
    return NetworkConfig(
        required_confirmations=required_confirmations, block_time=block_time, **kwargs
    )  # type: ignore


def _create_local_config(default_provider: Optional[str] = None) -> NetworkConfig:
    return _create_network_config(
        required_confirmations=0, block_time=0, default_provider=default_provider
    )


class FantomConfig(PluginConfig):
    opera: NetworkConfig = _create_network_config()
    opera_fork: NetworkConfig = _create_local_config()
    testnet: NetworkConfig = _create_network_config()
    testnet_fork: NetworkConfig = _create_local_config()
    local: NetworkConfig = _create_local_config(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Fantom(Ethereum):
    @property
    def config(self) -> FantomConfig:  # type: ignore
        return self.config_manager.get_config("fantom")  # type: ignore
