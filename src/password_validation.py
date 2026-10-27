
def is_valid_password(password):
    return (
        isinstance(password, str)
        and 8 <= len(password) <= 20
        and any(char.isdigit() for char in password)
    )
