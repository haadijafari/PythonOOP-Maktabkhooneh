from abc import ABC, abstractmethod
import random
from string import ascii_letters, digits


class Password(ABC):
    @abstractmethod
    def generate(self):
        pass


class PasswordChar(Password):
    pass_length = 20

    def generate(self):
        q_list = [random.choice(ascii_letters)
                  for i in range(self.pass_length)]
        return ''.join(q_list)


class PasswordInteger(Password):
    pass_length = 20

    def generate(self):
        q_list = [random.choice(digits) for i in range(self.pass_length)]
        return ''.join(q_list)


class PasswordCombo(Password):
    pass_length = 20

    def generate(self):
        q_list = [random.choice(ascii_letters + digits)
                  for i in range(self.pass_length)]
        return ''.join(q_list)


if __name__ == '__main__':
    p1 = PasswordChar()
    p2 = PasswordInteger()
    p3 = PasswordCombo()

    print(p1.generate(), p2.generate(), p3.generate(), sep='\n')
