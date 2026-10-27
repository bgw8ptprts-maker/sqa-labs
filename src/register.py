
USERS = ["existing_user"]


def validate_registration(login, password, email, age):
    errors = []

    # R1: логин 4–16 символов, латинские буквы,
    # цифры и подчёркивание
    if not isinstance(login, str) or not 4 <= len(login) <= 16:
        errors.append("Логин должен содержать от 4 до 16 символов")
    elif not all(
        char.isascii() and (char.isalnum() or char == "_")
        for char in login
    ):
        errors.append(
            "Логин может содержать только латинские буквы, цифры и _"
        )

    # R2: пароль 8–20 символов, заглавная буква и цифра
    if not isinstance(password, str) or not 8 <= len(password) <= 20:
        errors.append("Пароль должен содержать от 8 до 20 символов")
    else:
        if not any(char.isupper() for char in password):
            errors.append("Пароль должен содержать заглавную букву")
        if not any(char.isdigit() for char in password):
            errors.append("Пароль должен содержать цифру")

    # R3: ровно один @ и точка в домене
    if not isinstance(email, str):
        errors.append("Email должен быть строкой")
    elif (
        email.count("@") != 1
        or not email.split("@")[0]
        or "." not in email.split("@")[1]
        or email.split("@")[1].startswith(".")
        or email.split("@")[1].endswith(".")
    ):
        errors.append("Email должен содержать один @ и домен с точкой")

    # R4: целое число от 16 до 60 включительно
    if type(age) is not int or not 16 <= age <= 60:
        errors.append("Возраст должен быть целым числом от 16 до 60")

    # R5: логин должен быть уникальным
    if isinstance(login, str) and login in USERS:
        errors.append("Такой логин уже существует")

    # R6: собираем все ошибки, не останавливаясь на первой
    return errors
