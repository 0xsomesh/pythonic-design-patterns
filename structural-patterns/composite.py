from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Composite(Equipment):
    def __init__(self):
        self.equipments = []

    def get_price(self):
        price = 0
        for e in self.equipments:
            price = price + e.get_price()
        return price

    def add(self, equipment):
        self.equipments.append(equipment)

    def remove(self, equipment):
        self.equipments.remove(equipment)


class Leaf(Equipment):
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


if __name__ == '__main__':
    sim = Leaf(20)
    battery = Leaf(200)

    back_case = Composite()
    back_case.add(sim)
    back_case.add(battery)

    screen = Leaf(500)
    microphone = Leaf(350)

    front_case = Composite()
    front_case.add(screen)
    front_case.add(microphone)

    mobile_cover = Leaf(100)

    mobile = Composite()
    mobile.add(front_case)
    mobile.add(back_case)
    mobile.add(mobile_cover)

    print(mobile.get_price())
