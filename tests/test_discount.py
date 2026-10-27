
import pytest
from src.discount import discount


@pytest.mark.parametrize(
    "amount, expected",
    [
        (1, 0),
        (99_999, 0),
        (100_000, 5),
        (499_999, 5),
        (500_000, 10),
        (500_001, 10),
    ],
)
def test_discount_valid(amount, expected):
    assert discount(amount) == expected


@pytest.mark.parametrize("amount", [0, -1, 2.5, "abc", ""])
def test_discount_invalid(amount):
    with pytest.raises(ValueError):
        discount(amount)
