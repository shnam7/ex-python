class Animal:
  def __init__(self):
    print('Animal')


class Lion(Animal):
  def __init__(self):
    super().__init__()
    print('Lion')

class Tiger(Animal):
  def __init__(self):
    super().__init__()
    print('Tiger')

class Liger(Tiger, Lion):
  def __init__(self):
    super().__init__()
    print('Liger')

if __name__ == "__main__":
  liger = Liger()
