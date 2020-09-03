from random import choice


def search_exclusive(moto_list, market_id):
    for moto in moto_list:
        if moto.is_exclusive_to(market_id):
            return moto
        elif moto.has_exclusive():
            moto_list.remove(moto)
    return choice(moto_list)


def search_motoboy_by_id(moto_list, moto_id):
    for moto in moto_list:
        if str(moto.get_id()) == moto_id:
            return moto
    return False
