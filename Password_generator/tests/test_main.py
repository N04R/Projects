from src.password_generator import password_C
from src.password_generator import password_S
from src.password_generator import password_S_C
from src.password_generator import password_no_S_C
import pytest
import string

def test_password_C():
    password = password_C(15)
    assert len(password) == 15
    assert all(char in string.ascii_letters + string.digits + string.punctuation for char in password)
