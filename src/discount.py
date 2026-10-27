
def discount(amount):
    if type(amount) is not int or amount <= 0:
        raise ValueError("Amount must be a positive integer")

    if amount < 100_000:
        return 0
    elif amount < 500_000:
        return 5
    else:
        return 10
