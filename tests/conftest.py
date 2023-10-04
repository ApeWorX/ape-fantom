import ape
import pytest
from ape._cli import cli as ape_cli
from click.testing import CliRunner


@pytest.fixture
def networks():
    return ape.networks


@pytest.fixture
def accounts():
    return ape.accounts


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def cli():
    return ape_cli


@pytest.fixture
def fantom(networks):
    return networks.fantom


@pytest.fixture
def eth_tester_provider():
    if not ape.networks.active_provider or ape.networks.provider.name != "test":
        with ape.networks.fantom.local.use_provider("test") as provider:
            yield provider
    else:
        yield ape.networks.provider
