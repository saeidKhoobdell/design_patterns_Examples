#                               Example for <Observer> pattern Design
#                         *************************************************
from abc import ABC,abstractmethod

# our Notification Class
class Notify(ABC):
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notify):

    @staticmethod
    def send(message):
        print(f'Email send this message : {message}')

class SmsNotification(Notify):

    @staticmethod
    def send(message):
        print(f'Sms send this message : {message}')


def observer_pattern(message = ''):                  # our observer
    def decorator(func):
        def wrapped_function(obj, *args, **kwargs):
            result = func(obj, *args, **kwargs)
            for observer in obj.observers :
                observer.send(message)
            return result
        return wrapped_function
    return decorator


class Product:
    pass

class Payment:
    observers = [SmsNotification]

    @observer_pattern(message='complete  :)')
    def is_paid(self):
        pass


class Purchase:
    observers = [EmailNotification,SmsNotification]
    def __init__(self, products_list):
        self.products_list = products_list
        self.payment = Payment()

    def checkout(self):
        self.payment.is_paid()
    @observer_pattern(message='purchase canseled')
    def cancel(self):
        pass


if __name__ == '__main__':
    p1 = Product()
    p2 = Product()
    p3 = Product()
    p4 = Product()
    purchase = Purchase([p1,p2,p3,p4])
    purchase.cancel()
    print('*' * 20)
    purchase.checkout()