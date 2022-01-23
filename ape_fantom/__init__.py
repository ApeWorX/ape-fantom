from ape import plugins
from ape.api import NetworkAPI, create_network_type
from ape_geth import GethProvider
from ape_test import LocalNetwork

from .ecosystem import NETWORKS, Fantom, FantomConfig


@plugins.register(plugins.Config)
def config_class():
    return FantomConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Fantom


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "fantom", network_name, create_network_type(*network_params)

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield "fantom", "development", NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield "fantom", network_name, GethProvider

    yield "fantom", "development", LocalNetwork
