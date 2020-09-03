class Motoboy:
    def __init__(self, id: int, tax_value: int, exclusive_to: list = []):
        self.id = id
        self.tax_value = tax_value
        self.exclusive_to = exclusive_to
        self.orders = []

    def get_id(self) -> int:
        return self.id

    def get_tax_value(self) -> int:
        return self.tax_value

    def get_orders(self) -> list:
        return self.orders

    def has_order(self) -> bool:
        return self.orders != []

    def add_order(self, order):
        self.orders.append(order)

    def is_exclusive_to(self, market_id) -> bool:
        return market_id in self.exclusive_to

    def as_dict(self):
        return {
            'motoboy_id': self.id,
            'orders': self.get_orders(),
            'total': sum([order['delivery_tax'] for order in self.get_orders()])
        }


class Market:
    def __init__(self, id: int, extra_value: float):
        self.id = id
        self.extra_value = extra_value

    def get_id(self) -> int:
        return self.id

    def get_extra_value(self) -> float:
        return self.extra_value
