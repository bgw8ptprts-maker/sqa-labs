
import pytest
from src.password_validation import is_valid_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("abc12345", True),
        ("abc1234", False),             # длина < 8
        ("a" * 20 + "1", False),       # длина > 20
        ("abcdefgh", False),            # нет цифр
        ("a1", False),                  # короткий пароль и другие условия
        ("", False),
    ],
)
def test_password_validation(password, expected):
    assert is_valid_password(password) is expected
