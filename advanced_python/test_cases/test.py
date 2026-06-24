import sqlite3
import sys
import os
import pytest 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import (
    divide,
    get_weather,
    add,
    prime_number,
    get_season,
    UserManager,
    DatabaseManager,
    save_user
)

def test_cold_weather():
    assert get_weather(10) == "Cold"


def test_hot_weather():
    assert get_weather(30) == "Hot"


def test_add():
    assert add(10, 10) == 20


def test_divide():
    with pytest.raises(ValueError, match = "Can't divide by zero"):
        divide(10, 0)


"""
`@pytest.fixture`
    used to create reusable setup 
    code that can be shared across multiple tests.
"""
@pytest.fixture
def user_manager():
    """Creates a fresh instance of `UserManager()` for every test run"""
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("John Don", "john@gmail.com") == True 
    assert user_manager.get_user("John Don") == "john@gmail.com"


def test_for_duplicate_user(user_manager):
    user_manager.add_user("John Don", "john@gmail.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("John Don", "another@gmail.com")


@pytest.fixture
def database_manager():
    """
    Creates a fresh instance of `DataManager()` for
    every test run and clears the previour one
    """
    databaseManager = DatabaseManager()
    yield databaseManager
    databaseManager.data.clear()


def test_add_user(database_manager):
    database_manager.add_user("John", 1212)
    assert database_manager.get_user(1212) == "John"


def test_add_duplicate_user(database_manager):
    database_manager.add_user("John", 1212)
    with pytest.raises(ValueError, match="User already exists"):
        database_manager.add_user("Bob", 1212)


def test_delete_user(database_manager):
    database_manager.add_user("John", 1212)
    database_manager.delete_user(1212)
    assert database_manager.get_user(1212) != "John"
    assert database_manager.get_user(1212) is None


"""
`@pytest.mark.parameters()`
    used to run the same test function multiple 
    times with different input values.
"""
@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (19, True),
    (25, False),
])
def test_prime_number(num, expected):
    assert prime_number(num) == expected


"""Mocking"""
def test_get_season(mocker):
    # getting requests
    mocker_get = mocker.patch('main.requests.get')

    # setting the return values for testing
    mocker_get.return_value.status_code = 200
    mocker_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    # Call the function
    result = get_season("Dubai")

    # Assertions
    assert result == {"temperature": 25, "condition": "Sunny"}
    mocker_get.assert_called_once_with("https://api.weather.com/v1/Dubai")


"""Mocking with database"""
def test_save_user(mocker):
    mocker_get = mocker.patch("sqlite3.connect")
    mocker_cursor = mocker_get.return_value.cursor.return_value

    save_user("John", 35)

    mocker_get.assert_called_once_with("user.db")
    mocker_cursor.execute.assert_called_once_with(
        "INSERT  INTO users (name, age) VALUES (?,?)", ("John", 35)
    )