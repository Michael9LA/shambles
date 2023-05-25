from restaurant import Table
from unittest import main

table01 = Table(5)
table01.order("Risotto", 12.50, 2)
print(table01.bill)
table01.order("Burrito", 20.43, 3)
table01.remove("Burrito", 20.43, 2)
print(table01.bill)
print(table01.get_subtotal())
print(table01.get_total(0.15))
print(table01.split_bill())

# Run unit tests automatically
main(module='test_module', exit=False)
