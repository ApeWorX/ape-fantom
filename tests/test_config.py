from ape_ethereum.transactions import TransactionType

from ape_fantom.ecosystem import FantomConfig


def test_gas_limit(fantom):
    assert fantom.config.local.gas_limit == "max"


def test_default_transaction_type(fantom):
    assert fantom.config.opera.default_transaction_type == TransactionType.DYNAMIC


def test_opera_fork_not_configured():
    obj = FantomConfig.model_validate({})
    assert obj.opera_fork.required_confirmations == 0


def test_opera_fork_configured():
    data = {"opera_fork": {"required_confirmations": 555}}
    obj = FantomConfig.model_validate(data)
    assert obj.opera_fork.required_confirmations == 555


def test_custom_network():
    data = {"apenet": {"required_confirmations": 333}}
    obj = FantomConfig.model_validate(data)
    assert obj.apenet.required_confirmations == 333
