class Item:
    def __init__(self, itemName, itemType, unitPrice):
        self.itemName = itemName
        self.itemType = itemType
        self.unitPrice = unitPrice


class Store:
    def __init__(self, itemInventory):
        self.itemInventory = itemInventory  # itemInventory is a dictionary

    def buyItem(self, name_item, order_qty):
        for item, total_qty in self.itemInventory.items():
            if item.itemName.lower() == name_item.lower() and total_qty == 0:
                return None
            elif item.itemName.lower() == name_item.lower() and order_qty > total_qty:
                bill = total_qty * item.unitPrice
                self.itemInventory[item] = 0
                return bill
            elif item.itemName.lower() == name_item.lower() and order_qty <= total_qty:
                bill = order_qty * item.unitPrice
                self.itemInventory[item] = total_qty - order_qty
                return bill
        return None


if __name__ == "__main__":
    nop = int(input())
    item_inv = {}
    for p in range(nop):
        i_name = input()
        i_type = input()
        unit_p = int(input())
        i_stock = int(input())
        item_obj = Item(i_name, i_type, unit_p)
        item_inv[item_obj] = i_stock
    nor = int(input())
    order_d = {}
    for order in range(nor):
        o_name = input()
        o_qty = int(input())
        order_d[o_name] = o_qty

    store_obj = Store(item_inv)
    res_d = {}
    for m, n in order_d.items():
        bill_amt = store_obj.buyItem(m, n)
        res_d[m] = bill_amt
    for r, s in res_d.items():
        if s is None:
            print(f"{r} is not available")
        else:
            print(f"Bill of the item {r.lower()} = {s}")
    print("Stock in Hand:")
    for x, y in store_obj.itemInventory.items():
        print(f"{x.itemName} {y}")
