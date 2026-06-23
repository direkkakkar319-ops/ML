def get_weather(temp):
    if temp<20:
        return "Cold"
    return "Hot"

print(get_weather(30))


def add(a, b):
    return a+b 

print(add(10, 10))


def divide(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero")
    return a / b 

print(divide(10, 10))

class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True
    
    def get_user(self, username):
        return self.users.get(username)

class DatabaseManager:
    """Simulates a basic user database"""
    def __init__(self) -> None:
        self.data = {}
    
    def add_user(self, username, user_id):
        if user_id in self.data:
            raise ValueError("User already exists")
        self.data[user_id] = username
    
    def get_user(self, user_id):
            return self.data.get(user_id, None)
    
    def delete_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]

"""Parameterised testing"""
def prime_number(n):
    if n<2:
        return False 
    elif n==2 or n==3:
        return True  
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

"""
Mocking(MOCKS)
    When we write the code there can be times when part 
    of code relies on something that is not active in 
    in testing environment

    Then we would mock or create a fake version of that 
    dependency
"""
import requests

def get_season(country):
    response = requests.get(f"https://api.weather.com/v1/{country}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch data")

"""
Mocking for the database
"""
import sqlite3

def save_user(name, age):
    conn = sqlite3.connect("user.db")

    cursor = conn.cursor()
    cursor.execute("INSERT  INTO users (name, age) VALUES (?,?)", (name, age))
    conn.commit()
    conn.close()