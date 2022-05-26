import random


class User:
  def __init__(self,name):
    self.name = name
  def __str__(self):
    return self.name
class Dice:

  @staticmethod
  def roll():
    return random.randint(1,6)

def check_permission(func):
  def wrapped_func(game, user):
      if game.turn == user:
         game.change()
         return func(game)
      return f'thats turn {game.turn}'
  return wrapped_func

class Game:
  def __init__(self, user1, user2):
    self.user1 =user1
    self.user2 = user2
    self.turn = user1
    self.dice = Dice

  def change(self):
      self.turn = self.user2 if self.turn == self.user1 else self.user1
  @check_permission
  def roll_dice(self):
      return self.dice.roll()





if __name__ == '__main__' :
    u1 = User('user1')
    u2 = User('user2')

    game = Game(u1,u2)
    print(game.roll_dice(u1))
    print(game.roll_dice(u2))
    print(game.roll_dice(u1))
    print(game.roll_dice(u1))
    print(game.roll_dice(u2))
    print(game.roll_dice(u1))