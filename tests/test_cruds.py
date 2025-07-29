from src.hash_table import HashTable
import pytest


@pytest.fixture
def hash_table() -> HashTable:
    hash_table = HashTable()
    hash_table.put(3, 'Один')
    hash_table.put(11, 'Два')
    hash_table.put(19, 'Три')
    return hash_table


def test_put(hash_table):
    hash_table.put('skldjfsjfds', 'четыре')
    assert hash_table.get('skldjfsjfds').value == 'четыре'


def test_get(hash_table):
    assert hash_table.get(11).value == 'Два'
    assert hash_table.get(19).value == 'Три'
    assert hash_table.get('kashdf;asdf;lsadf') is None


def test_remove(hash_table):
    hash_table.remove(19)
    hash_table.remove('skldjfsjfds')
    assert hash_table.get(19) is None
    assert hash_table.get('skldjfsjfds') is None