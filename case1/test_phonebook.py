import pytest

from case1.phonebook import Phonebook


def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_contain_all_names():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.get_names()


def test_missing_name_raises_error():
    phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("Missing")

