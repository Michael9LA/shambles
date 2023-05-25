class Table:

    def __init__(self, no_of_people):
        self.no_of_people = no_of_people
        self.bill = []

    def order(self, item: str, price: float, quantity: int = 1):
        self.item = item
        self.price = price
        self.quantity = quantity

        order_info = {"item": item, "price": f'£{price}', "quantity": quantity}
        self.bill.append(order_info)

        if self.item in order_info:
            order_info["quantity"] += quantity
            self.bill.append(order_info)

    def remove(self, item: str, price: float, quantity: int = 1) -> bool:
        self.item = item
        self.price = price
        self.quantity = quantity

        order_info = self.bill
        for item in order_info:
            items = item['item']
            prices = item['price']
            amount = item['quantity']
            if items == self.item and prices == self.price:
                if amount != self.quantity:
                    self.bill["quantity"] -= quantity
                    order_info.append(amount)
                if self.quantity <= 0:
                    self.bill.remove({"item": item, "price": f'£{price}', "quantity": quantity})
                    return False
                else:
                    self.bill["quantity"] -= quantity
                    return True

    def get_subtotal(self, service_charge: float = 0.10):
        subtotal = 0
        for item in self.bill:
            subtotal += item['price'] * item['quantity']

    def get_total(self, service_charge: float = 0.10):
        return{
            'Sub Total': f'£{self.get_subtotal()}',
            'Service Charge': f'£{self.get_subtotal() * service_charge}',
            'Total': f'£{self.get_subtotal() * service_charge + self.get_subtotal() * service_charge}'
        }

    def split_bill(self):
        pass
        # subtotal = self.get_subtotal()
        # return round(subtotal / self.no_of_people, 2)
