import items

class shopping_cart:
    def __init__(self):
        self.shopping_list = {}

    def __str__(self):
        return f"{self.shopping_list}"

    def add_item(self, purchase_item):
        if purchase_item.name in self.shopping_list:
            self.shopping_list[purchase_item.name]['quantity'] += 1
        else:
            self.shopping_list[purchase_item.name] = {'quantity': 1, 'base_price': purchase_item.price, 'tax_rate': purchase_item.tax}

    def remove_item(self, remove_item):
        if remove_item.name in self.shopping_list:
            if self.shopping_list[remove_item.name]['quantity'] > 1:
                self.shopping_list[remove_item.name]['quantity'] -= 1
            elif self.shopping_list[remove_item.name]['quantity'] == 1:
                self.shopping_list.pop(remove_item.name, None)
        else:
            print(f"{remove_item.name} was not in shopping cart in the first place")
    
    def calc_total_base_price(self):
        total = 0
        for k in self.shopping_list:
            total += self.shopping_list[k]['base_price'] * self.shopping_list[k]['quantity']
        return total

    def calc_taxed_price(self):
        tax_total = 0
        for k in self.shopping_list:
            if self.shopping_list[k]['tax_rate'] == 'standard':
                tax_total += self.shopping_list[k]['base_price'] * self.shopping_list[k]['quantity'] * 1.1
            elif self.shopping_list[k]['tax_rate'] == 'imported':
                tax_total += self.shopping_list[k]['base_price'] * self.shopping_list[k]['quantity'] * 1.2
            else:
                tax_total += self.shopping_list[k]['base_price'] * self.shopping_list[k]['quantity'] 
        return tax_total

item1 = items.buy_item('Cookies', 10, 'standard')
item2 = items.buy_item('Bananas', 5, 'exempt')
item3 = items.buy_item('Spaghetti', 5, 'imported')

new_cart = shopping_cart()
print(new_cart)

# Testing that add function is working as intended
my_cart = shopping_cart()
my_cart.add_item(item1)
my_cart.add_item(item1)
my_cart.add_item(item2)
print(my_cart)
print('')

# Testing total base price calculation function
print(my_cart.calc_total_base_price())
print('')

# Testing taxed price calculation function
print(my_cart.calc_taxed_price())
print('')

# Testing to see that the remove function is working as intended
my_cart.remove_item(item1) # Should remove 1 quantity of cookies
my_cart.remove_item(item2) # Should delete bananas from shopping cart
my_cart.remove_item(item3) # Should print message saying bananas doesn't exist
print(my_cart) 
print('')