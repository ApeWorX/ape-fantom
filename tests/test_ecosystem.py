import pytest
from ape_ethereum.transactions import TransactionType


def test_gas_limit(networks):
    fantom = networks.fantom
    assert fantom.config.local.gas_limit == "max"


@pytest.mark.parametrize("type", (0, "0x0"))
def test_create_transaction(networks, type):
    fantom = networks.fantom
    txn = fantom.create_transaction(type=type)
    assert txn.type == TransactionType.STATIC.value
