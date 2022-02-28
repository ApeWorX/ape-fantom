import pytest


@pytest.fixture
def networks():
    from ape import networks

    return networks


@pytest.fixture
def accounts():
    from ape import accounts

    return accounts


@pytest.fixture
def Contract():
    from ape import Contract

    return Contract


def test_basic(accounts, networks):

    with networks.fantom.local.use_provider("test"):
        a = accounts.test_accounts[0]
        a.transfer(a, 100)


def test_connection(Contract, networks):
    with networks.fantom.opera.use_provider("geth"):
        a = Contract("0x0000000000000000000000000000000000000000")
        assert a.balance > 915  # NOTE: Anything sent to 0x0 is lost forever
