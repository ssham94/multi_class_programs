class buy_item:

    def __init__(self, item_name, item_price, tax_rate):
        self.name = item_name
        self.price = item_price
        self.tax = tax_rate

    def __str__(self):
        return f"Name: {self.name}, price: {self.price}, tax type: {self.tax}"