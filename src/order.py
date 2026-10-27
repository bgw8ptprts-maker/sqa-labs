
class Order:
    NEW = "NEW"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

    def __init__(self):
        self.status = self.NEW

    def _transition(self, expected, target):
        if self.status != expected:
            raise ValueError(
                f"Cannot transition from {self.status} to {target}"
            )
        self.status = target

    def pay(self):
        self._transition(self.NEW, self.PAID)

    def ship(self):
        self._transition(self.PAID, self.SHIPPED)

    def deliver(self):
        self._transition(self.SHIPPED, self.DELIVERED)

    def cancel(self):
        if self.status not in (self.NEW, self.PAID):
            raise ValueError(
                f"Cannot cancel order in status {self.status}"
            )
        self.status = self.CANCELLED
