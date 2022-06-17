def test_basic(accounts, networks):
    with networks.fantom.local.use_provider("test"):
        account = accounts.test_accounts[0]
        account.transfer(a, 100)
