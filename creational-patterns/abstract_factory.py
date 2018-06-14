from abc import ABC, abstractmethod


class AbstractPhoneFactory(ABC):
    @abstractmethod
    def battery(self):
        pass

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def cover(self):
        pass


class ApplePhoneFactory(AbstractPhoneFactory):
    def battery(self):
        return 200

    def screen(self):
        return 200

    def cover(self):
        return 200


class SamsungPhoneFactory(AbstractPhoneFactory):
    def battery(self):
        return 100

    def screen(self):
        return 100

    def cover(self):
        return 100


class MyCompany:
    def __init__(self):
        self.cost = 0

    def make_phone(self, factory):
        factory = factory()
        self.cost = factory.battery() + factory.screen() + factory.cover()

    def total_cost(self):
        return self.cost


if __name__ == '__main__':
    apple_company = MyCompany()
    apple_company.make_phone(ApplePhoneFactory)
    print(apple_company.total_cost())

    samsung_company = MyCompany()
    samsung_company.make_phone(SamsungPhoneFactory)
    print(samsung_company.total_cost())
