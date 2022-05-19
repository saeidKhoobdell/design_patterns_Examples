#                            Example for <Factory> design pattern
#                      **************************************************

from abc import ABC, abstractmethod
from random import choice

CHOISES = ['r', 's', 'p']

class Player(ABC):

  @abstractmethod
  def move(self):
    return

class HumanPlayer(Player):
      def move(self):
          return


class SystemPlayer(Player):
      def move(self):
        return


class Game():       # actually here is my Factory :)
  @staticmethod
  def play():
    PLAY_TYPES = {
      's': 'single play',
      'm': 'multiple play'
    }
    for type in PLAY_TYPES:
      print('press', type, 'for', PLAY_TYPES[type])
    game_type = input('single or multiple ?')
    if game_type == 's' :
       p1 = HumanPlayer()
       p2 = SystemPlayer()
    elif game_type == 'm' :
       p1 = HumanPlayer()
       p2 = HumanPlayer()
    else:print('Oops! invalid input : ' )

    return p1 ,p2


if __name__ == '__main__':
    player1, player2 = Game.play()
    for p in [player1, player2]:
        p.move()

