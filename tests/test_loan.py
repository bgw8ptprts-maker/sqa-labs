
import pytest

from src.loan import loan_decision


@pytest.mark.parametrize(
    "age, income, overdue, expected",
    [
        # Все 8 правил полной таблицы
        (35, 6_000_000, False, "approve"),
        (35, 6_000_000, True, "reject"),
        (35, 3_000_000, False, "guarantor"),
        (35, 3_000_000, True, "reject"),
        (20, 6_000_000, False, "reject"),
        (20, 3_000_000, False, "reject"),
        (20, 6_000_000, True, "reject"),
        (20, 3_000_000, True, "reject"),

        # Границы возраста
        (20, 6_000_000, False, "reject"),
        (21, 6_000_000, False, "approve"),
        (60, 6_000_000, False, "approve"),
        (61, 6_000_000, False, "reject"),

        # Границы дохода
        (35, 4_999_999, False, "guarantor"),
        (35, 5_000_000, False, "approve"),
    ],
)
def test_loan_rules(age, income, overdue, expected):
    assert loan_decision(age, income, overdue) == expected
