from abc import ABC, abstractmethod

class Compositor(ABC):
    @abstractmethod
    def printx(self):
        pass

class Print_a(Compositor):
    def printx(self):
        print('a')

class Print_b(Compositor):
    def printx(self):
        print('b')

class Composition:
    def __init__(self, compositor):
        self.compositor = compositor

    def excecute(self):
        self.compositor.printx()

if __name__ == '__main__':
    c1 = Composition(Print_a())
    c2 = Composition(Print_b())

    print('c1 with compositor Print_a prints ')
    c1.excecute()
    print('c2 with compositor Print_b prints ')
    c2.excecute()
