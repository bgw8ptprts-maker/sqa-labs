"""Calculate a letter grade from numeric marks."""

GRADE_THRESHOLDS = {
    "A": 86,
    "B": 71,
    "C": 56,
}


def calc_grade(marks, bonus=0):
    """Return a letter grade or None for invalid input."""
    if not marks:
        return None

    total = 0
    for mark in marks:
        if not 0 <= mark <= 100:
            return None
        total += mark

    average = total / len(marks) + bonus

    for grade, threshold in GRADE_THRESHOLDS.items():
        if average >= threshold:
            return grade

    return "F"
