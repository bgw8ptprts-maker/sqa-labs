
def grade(score):
    if type(score) is not int or not 0 <= score <= 100:
        raise ValueError("Score must be an integer from 0 to 100")

    if score <= 54:
        return 2
    elif score <= 69:
        return 3
    elif score <= 84:
        return 4
    else:
        return 5
