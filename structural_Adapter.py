#                                  example for <Adapter> pattern Design
#                              ********************************************

class Mobile:                              # our product
  def __init__(self, name, price):
    self.name = name
    self.price = price


class Adapter:              # our Adapter
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):

        return  self.rate * product.price


if __name__ == '__main__':
    m1 = Mobile('apple_13promax', 1300)
    m2 = Mobile('samsung_21', 1300)
    m3 = Mobile('apple_12', 1200)
    products = [m1, m2, m3]
    adapter = Adapter(28000)
    for product in products :
      print(f'{product.name} : {adapter.exchange(product)} Toman')