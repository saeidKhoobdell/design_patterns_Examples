#                                        Example for <Lazy Loader>
#                                    *********************************
from time import sleep

class LazyLoader:                         # our Lazer Loader (that means the class call when we initiate that class)
    def __init__(self,cls):
      self.cls = cls
      self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)
        



class MySQLHhandler:
    def __init__(self):
      sleep(1)

    def get(self):
      return 'hello from Sql'


class MongoLHandler:
    def __init__(self):
      sleep(100)
    def get(self):
      return 'hello from Mongo'

class NotificationCenterHandler:
    def __init__(self):
      sleep(100)

    def get(self):
      return 'hello from Notif'


if __name__ == "__main__" :
    sql = LazyLoader(MySQLHhandler)
    mongo = LazyLoader(MongoLHandler)
    notif = LazyLoader(NotificationCenterHandler)
    
    print(sql.get())                          #   we initiate just sql and so we dont need 100s mongo and notif