
def loan_decision(age: int, income: int, overdue: bool) -> str:
    age_valid = 21 <= age <= 60
    income_valid = income >= 5_000_000
    no_overdue = not overdue

    if age_valid and no_overdue and income_valid:
        return "approve"

    if age_valid and no_overdue and not income_valid:
        return "guarantor"

    return "reject"
