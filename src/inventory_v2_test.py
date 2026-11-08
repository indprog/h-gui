from datetime import datetime, timedelta

from inventory_v2 import *

item1 = Item(id="hydraulic pump", price_per_unit=Decimal("20"))
item2 = BulkItem(
    id="lubrication oil",
    price_per_unit=Decimal("10.1"),
    unit_weight=Decimal("0.9"),
    measurement_unit="l",
)
item3 = HardItem(id="pen", price_per_unit=Decimal("1.1"), unit_weight=Decimal(".001"))
item4 = LicenseItem(
    id="Power Plus",
    price_per_unit=Decimal("10_000"),
    validity_duration=timedelta(weeks=52),
)

inventory = Inventory()
inventory.stock = {
    item1: Decimal("10"),
    item2: Decimal("1"),
    item3: Decimal("500"),
    item4: Decimal("Infinity"),
}

order_line1 = OrderLine(item=item1, quantity=Decimal("4"))
order_line2 = OrderLine(item=item2, quantity=Decimal("2.1"))
order_line3 = OrderLine(item=item3, quantity=Decimal("100"))
order_line4 = OrderLine(item=item4, quantity=Decimal("5"))

order1 = Order(time=datetime.now() - timedelta(days=3), order_lines=[order_line1])
order2 = Order(
    time=datetime.now() - timedelta(days=2),
    order_lines=[order_line1, order_line2, order_line3],
)
order3 = Order(time=datetime.now(), order_lines=[order_line2])
order4 = Order(time=datetime.now(), order_lines=[order_line4])

customer1 = Customer(id="Ramanda")
customer2 = Customer(id="Totoro")

order_book = OrderBook(inventory)
customer1.create_order(order_book, order1)
customer2.create_order(order_book, order2)
customer2.create_order(order_book, order3)
customer1.create_order(order_book, order4)


def process_order():
    if order_book.process_next_order():
        print("Order processed.")
    else:
        print("Order cannot be fulfilled or there are no orders left.")
    print(f"Total revenue: {order_book.total_revenue()}")
    print()


process_order()
process_order()

print("Filling up stock")
inventory.stock[item2] += 10

process_order()
process_order()
process_order()
process_order()
