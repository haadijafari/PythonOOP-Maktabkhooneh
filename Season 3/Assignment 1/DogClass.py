class Dog:
    __quantity = 0

    def __init__(self, name: str(), age: int()):
        self.name = name.title()
        self.age = age
        Dog.__quantity += 1

    @classmethod
    def dogCount(cls):
        return cls.__quantity


if __name__ == '__main__':
    bulldog = Dog('Sammy', 3)
    hosky = Dog('Alex', 5)
    hosky.quantity = 1
    print(Dog.dogCount())
    print(hosky.quantity)
