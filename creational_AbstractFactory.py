#                           example for <Abstract Factory> design pattern
#                      *******************************************************
from abc import ABC, abstractmethod


class ProductBase(ABC):

  @abstractmethod
  def price(self):
    pass
  @abstractmethod
  def detail(self):
    pass




class DetailBase(ABC):
  @abstractmethod
  def show(self):
    pass


class RugsPrice(DetailBase):
  def __init__(self,rugs):
    self.rugs = rugs
  def show(self):
    print(self.rugs._price)


class GiftcardPrice(DetailBase):
  def __init__(self,giftcard):
    self.giftcard = giftcard
  def show(self):
    print("from:",self.giftcard.min_price,'$  to  :', self.giftcard.max_price,'$')


class RugsDetail(DetailBase):
  def __init__(self,rugs):
    self.rugs = rugs
  def show(self):
    print(self.rugs._name)


class GiftcardDetail(DetailBase):
  def __init__(self, giftcard):
    self.giftcard = giftcard
  def show(self):
    print(self.giftcard.company)



class Rugs(ProductBase):
    def __init__(self,name, price):
      self._name = name
      self._price = price

    @property
    def price(self):
      return RugsPrice(self)

    @property
    def detail(self):
      return RugsDetail(self)


class Giftcard(ProductBase,):
  def __init__(self, company, min_price, max_price):
    self.company = company
    self.min_price=min_price
    self.max_price = max_price

  @property
  def price(self):
    return GiftcardPrice(self)

  @property
  def detail(self):
    return GiftcardDetail(self)

if __name__ == '__main__':
    r1 = Rugs('persian',6500)
    r2 = Rugs('turkish',4500)
    g1 = Giftcard('Apple',10,60)
    g2 = Giftcard('Amazon',10, 100)

    pruducts= [r1,r2,g1,g2]
    for pruduct in pruducts:
        pruduct.detail.show()
        pruduct.price.show()
        print('*' * 10)