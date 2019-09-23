import pytest

from case1.phonebook import Phonebook


@pytest.fixture
def phonebook():
    return Phonebook()


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_contain_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.get_names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Missing")

