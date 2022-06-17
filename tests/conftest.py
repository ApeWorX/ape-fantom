import pytest
import ape


@pytest.fixture
def networks():
    return ape.networks


@pytest.fixture
def accounts():
    return ape.accounts

