
import pytest

from src.order import Order


@pytest.mark.parametrize(
    "actions, expected",
    [
        (["pay"], Order.PAID),
        (["cancel"], Order.CANCELLED),
        (["pay", "ship"], Order.SHIPPED),
        (["pay", "cancel"], Order.CANCELLED),
        (["pay", "ship", "deliver"], Order.DELIVERED),
    ],
)
def test_valid_transitions(actions, expected):
    order = Order()

    for action in actions:
        getattr(order, action)()

    assert order.status == expected


@pytest.mark.parametrize(
    "actions, invalid_action",
    [
        ([], "ship"),
        ([], "deliver"),
        (["pay"], "deliver"),
        (["pay", "ship"], "cancel"),
        (["pay", "ship", "deliver"], "pay"),
        (["cancel"], "pay"),
        (["cancel"], "cancel"),
    ],
)
def test_invalid_transitions(actions, invalid_action):
    order = Order()

    for action in actions:
        getattr(order, action)()

    old_status = order.status

    with pytest.raises(ValueError):
        getattr(order, invalid_action)()

    assert order.status == old_status