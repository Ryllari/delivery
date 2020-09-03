# Started at 01/Set/2020 - 21:12
# Finished at 01/Set/2020 - 22:42

import sys
from pprint import pprint

from actors import Motoboy, Market
from utils import search_exclusive, search_motoboy_by_id

# Creating Motoboys
moto1 = Motoboy(1, 2)
moto2 = Motoboy(2, 2)
moto3 = Motoboy(3, 2)
moto4 = Motoboy(4, 2, [1])
moto5 = Motoboy(5, 3)

motoboys = [moto1, moto2, moto3, moto4, moto5]

# Creating Markets
market1 = Market(1, 0.05)
market2 = Market(2, 0.05)
market3 = Market(3, 0.15)

# Creating orders
orders = [
    {'order_number': 1, 'value': 50, 'market': market1},
    {'order_number': 2, 'value': 50, 'market': market1},
    {'order_number': 3, 'value': 50, 'market': market1},

    {'order_number': 1, 'value': 50, 'market': market2},
    {'order_number': 2, 'value': 50, 'market': market2},
    {'order_number': 3, 'value': 50, 'market': market2},
    {'order_number': 4, 'value': 50, 'market': market2},

    {'order_number': 1, 'value': 50, 'market': market3},
    {'order_number': 2, 'value': 50, 'market': market3},
    {'order_number': 3, 'value': 100, 'market': market3},
]

# Managing orders
available_motos = motoboys.copy()
for order in orders:
    market = order['market']
    motoboy = search_exclusive(available_motos, market.get_id())
    available_motos.remove(motoboy)

    delivery_tax = order['value'] * market.get_extra_value() + motoboy.get_tax_value()
    order.update({'delivery_tax': delivery_tax, 'market': market.id})
    motoboy.add_order(order)

    if not available_motos:
        available_motos = motoboys.copy()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        motoboy = search_motoboy_by_id(motoboys, sys.argv[1])
        if motoboy:
            pprint(motoboy.as_dict())
        else:
            print('Invalid motoboy id')
    else:
        pprint([motoboy.as_dict() for motoboy in motoboys])
