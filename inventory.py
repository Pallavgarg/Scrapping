class InsufficientException(Exception):
    pass


class MobileInventory:
    balance_inventory = {}
    def __init__(self, inventory=None):
        if not inventory:
            MobileInventory.balance_inventory = {}
        else:
            if not isinstance(inventory, dict):
                raise TypeError("Input inventory must be a dictionary")
            elif not (set(map(type, inventory)) == {str}):
                raise ValueError("Mobile model name must be a string")
            else:
                for i in inventory.values():
                    if isinstance(i, int) and i > 0:
                        pass
                    else:
                        raise ValueError("No. of mobiles must be a positive integer")
            MobileInventory.balance_inventory = inventory

    @classmethod
    def add_stock(cls, new_stock):
        print("before update")
        print(cls.balance_inventory)
        if not isinstance(new_stock, dict):
            raise TypeError("Input stock must be a dictionary")
        elif not (set(map(type, new_stock)) == {str}):
            raise ValueError("Mobile model name must be a string")
        else:
            for i in new_stock.values():
                if isinstance(i, int) and i > 0:
                    pass
                else:
                    raise ValueError("No. of mobiles must be a positive integer")

        for key, value in new_stock.items():
            if key in cls.balance_inventory.keys():
                x = cls.balance_inventory[key] + value
                cls.balance_inventory[key] = x
            else:
                cls.balance_inventory.update({key: value})
        print(new_stock)
        print("after update")
        print(cls.balance_inventory)


    @classmethod
    def sell_stock(cls, requested_stock):
        if not isinstance(requested_stock, dict):
            raise TypeError("Requested stock must be a dictionary")
        elif not (set(map(type, requested_stock)) == {str}):
            raise ValueError("Mobile model name must be a string")
        else:
            for i in requested_stock.values():
                if isinstance(i, int) and i > 0:
                    pass
                else:
                    raise ValueError("No. of mobiles must be a positive integer")
        for key, value in requested_stock.items():
            if key in cls.balance_inventory.keys():
                if cls.balance_inventory[key] < value:
                    raise InsufficientException("Insufficient Stock")
                else:
                    y = cls.balance_inventory[key] - value
                    cls.balance_inventory[key] = y
            else:
                raise InsufficientException("No Stock. New Model Request")