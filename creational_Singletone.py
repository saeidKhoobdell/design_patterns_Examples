#                            Example for <Singletone> Design pattern
#                        ***************************************************


class Singletone:
  def __new__(cls, *args, **kwargs):
    if not hasattr(cls, 'instance'):
      cls.instance = super(*args, **kwargs)
    return cls.instance


if __name__ == '__main__':
  s1 = Singletone()
  s2 = Singletone()
  s3 = Singletone()
  print(id(s1) == id(s2) == id(s3))