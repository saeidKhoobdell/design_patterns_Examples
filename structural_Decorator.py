#                              Example for <Decorator> Pattern Design
#                          **********************************************

COUNTRY = ['IRAN','UAE']
VAT = {
    'IRAN' : 9,
    'UAE' : 12
}
class User:
    pass


class Address:
    def __init__(self, country):
        self.country = country


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:

    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.products_list = []

    def add_product(self, products_list):
        if not isinstance(products_list, list):
            products_list = [products_list]
        self.products_list.extend(products_list)

    def sum(self):
        s = 0
        for product in self.products_list:
            s += product.price
        return s

                     #  creat our Decorator pattern Designe with decorator tool in python


def calculate_vat(func):
    def wrapped_function(purchase):
        vat = VAT[purchase.address.country]
        total_price = purchase.sum()
        return total_price + total_price * (vat / 100)
    return wrapped_function


def show_total_price(purchase):
    return purchase.sum()

@calculate_vat
def show_price_with_vat(purchase):
    return purchase.sum()


if __name__ == '__main__':

    u1 = User()

    address_iran = Address(COUNTRY[0])

    address_uae = Address(COUNTRY[1])

    p1 = Product('persian Saffron', 170000)
    p2 = Product('persian Tea', 80000)
    p3 = Product('persian Honey', 320000)
    basket = [p1, p2]

    purchase_1 = Purchase(u1, address_iran)

    purchase_2 = Purchase(u1 , address_uae)

    purchase_1.add_product([p1, p3])
    purchase_2.add_product(p3)

    show_price_with_vat(purchase_2)
    print(show_price_with_vat(purchase_2))