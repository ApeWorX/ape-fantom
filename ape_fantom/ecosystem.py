from typing import Optional, Type, cast

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.utils import DEFAULT_LOCAL_TRANSACTION_ACCEPTANCE_TIMEOUT
from ape_ethereum.ecosystem import Ethereum, ForkedNetworkConfig, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "opera": (250, 250),
    "testnet": (4002, 4002),
}


def _create_config(
    required_confirmations: int = 1, block_time: int = 1, cls: Type = NetworkConfig, **kwargs
) -> NetworkConfig:
    return cls(required_confirmations=required_confirmations, block_time=block_time, **kwargs)


def _create_local_config(default_provider: Optional[str] = None, use_fork: bool = False, **kwargs):
    return _create_config(
        block_time=0,
        default_provider=default_provider,
        gas_limit="max",
        required_confirmations=0,
        transaction_acceptance_timeout=DEFAULT_LOCAL_TRANSACTION_ACCEPTANCE_TIMEOUT,
        cls=ForkedNetworkConfig if use_fork else NetworkConfig,
        **kwargs,
    )


class FantomConfig(PluginConfig):
    opera: NetworkConfig = _create_config()
    opera_fork: ForkedNetworkConfig = _create_local_config(use_fork=True)
    testnet: NetworkConfig = _create_config()
    testnet_fork: ForkedNetworkConfig = _create_local_config(use_fork=True)
    local: NetworkConfig = _create_local_config(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Fantom(Ethereum):
    @property
    def config(self) -> FantomConfig:  # type: ignore[override]
        return cast(FantomConfig, self.config_manager.get_config("fantom"))
