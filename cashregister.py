class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.append({"item": item_name, "price": price, "quantity": quantity})

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"Discount applied: {self.discount}% off, Total: ${self.total:.2f}"
        else:
            return "No discount applied."

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item["price"] * last_item["quantity"]
            self.last_transaction = -(last_item["price"] * last_item["quantity"])
        else:
            return "No transactions to void."

    def get_total(self):
        return f"Total: ${self.total:.2f}"

    def get_items(self):
        return self.items

    def get_discount(self):
        return self.discount

    def get_last_transaction(self):
        return self.last_transaction
