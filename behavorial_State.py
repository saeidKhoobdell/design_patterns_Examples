#                              Example for < State> Pattern Design
#                         *********************************************
from abc import ABC, abstractmethod


class Message:
  def __init__(self,subject,content, sender):
    self.subject = subject
    self.content = content
    self.sender = sender
    self.flow = [sender]
  @property
  def current(self):
    return self.flow[-1]
  def send(self,to_user):
    if to_user.__class__ not in self.current.allow:
      print(f'sorry ! <{self.current.name}> is not allowed to send Email to  <{to_user.name}>')
    else :
      self.flow.append(to_user)
      print(f"The Message from <{self.current.name}> sent to <{to_user.name}>")


class User(ABC):
    @property
    @abstractmethod
    def allow(self):
      pass

class ManagerDirector(User):
    allow =[]

    @property
    def name(self):
      return 'manager Director'


class InternalManager(User):
  allow = []

  @property
  def name(self):
    return 'Internal Manger'

class Superviser(User):
  allow = [InternalManager]

  @property
  def name(self):
    return 'Supervisor'

class Operator(User):
  allow = [Superviser]

  @property
  def name(self):
    return 'Operator'
class Client(User):
  allow = [Operator]

  @property
  def name(self):
    return 'Client'

if __name__ == '__main__':
  mnd=ManagerDirector()
  inm=InternalManager()
  spr=Superviser()
  opt=Operator()
  clt=Client()
  message = Message('issue #1', 'issue description',clt)
  message.send(opt)
  message.send(spr)
  message.send(mnd)