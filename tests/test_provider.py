def test_use_provider(accounts, networks):
    with networks.fantom.local.use_provider("test"):
        account = accounts.test_accounts[0]
        account.transfer(account, 100)
