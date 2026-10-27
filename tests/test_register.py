
import pytest
from src.register import validate_registration


# Все тесты этого модуля входят в regression
pytestmark = pytest.mark.regression


# TC-REG-001
@pytest.mark.smoke
def test_register_valid():
    assert validate_registration(
        "ali_01", "Secret2026", "ali@kiut.uz", 20
    ) == []


# TC-REG-002
def test_login_too_short():
    errors = validate_registration(
        "ali", "Secret2026", "ali@kiut.uz", 20
    )
    assert any("Логин" in error for error in errors)


# TC-REG-003
def test_login_invalid_character():
    errors = validate_registration(
        "ali-01", "Secret2026", "ali@kiut.uz", 20
    )
    assert any("Логин" in error for error in errors)


# TC-REG-004, TC-REG-005, TC-REG-006
@pytest.mark.parametrize(
    "password, expected_error",
    [
        ("secret2026", "заглавную букву"),
        ("SecretWord", "цифру"),
        ("Sec1", "от 8 до 20"),
        ("SecretWord12345678901", "от 8 до 20"),
    ],
)
def test_password_validation(password, expected_error):
    errors = validate_registration(
        "ali_02", password, "ali2@kiut.uz", 20
    )
    assert any(expected_error in error for error in errors)


# TC-REG-007
def test_invalid_email():
    errors = validate_registration(
        "ali_03", "Secret2026", "ali.kiut.uz", 20
    )
    assert any("Email" in error for error in errors)


# TC-REG-008
def test_age_too_low():
    errors = validate_registration(
        "ali_04", "Secret2026", "ali4@kiut.uz", 15
    )
    assert any("Возраст" in error for error in errors)


# TC-REG-009
@pytest.mark.smoke
def test_duplicate_login():
    errors = validate_registration(
        "existing_user", "Secret2026", "new@kiut.uz", 20
    )
    assert any("уже существует" in error for error in errors)

# TC-REG-010
@pytest.mark.smoke
def test_multiple_invalid_fields():
    errors = validate_registration(
        "ab-", "secret", "wrong-email", 20
    )
    assert any("Логин" in error for error in errors)
    assert any("Пароль" in error for error in errors)
    assert any("Email" in error for error in errors)
