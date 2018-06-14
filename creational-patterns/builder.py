from abc import ABC, abstractmethod


class Phone(object):
    def __init__(self):
        self.cost = 0

    def add(self, price):
        self.cost = self.cost + price

    def get_cost(self):
        return self.cost


class AbstractPhoneBuilder(ABC):
    @abstractmethod
    def add_battery(self):
        pass

    @abstractmethod
    def add_screen(self):
        pass


class ApplePhoneBuilder(AbstractPhoneBuilder):
    def __init__(self):
        self.phone = Phone()

    def add_battery(self):
        self.phone.add(200)

    def add_screen(self):
        self.phone.add(200)

    def get_phone(self):
        return self.phone


class SamsungPhoneBuilder(AbstractPhoneBuilder):
    def __init__(self):
        self.phone = Phone()

    def add_battery(self):
        self.phone.add(100)

    def add_screen(self):
        self.phone.add(100)

    def get_phone(self):
        return self.phone


class MyCompany:
    def make_phone(self, builder):
        builder = builder()
        builder.add_battery()
        builder.add_screen()
        return builder.get_phone()


if __name__ == '__main__':
    apple_company = MyCompany()
    apple_phone = apple_company.make_phone(ApplePhoneBuilder)
    print(apple_phone.get_cost())

    samsung_company = MyCompany()
    samsung_phone = samsung_company.make_phone(SamsungPhoneBuilder)
    print(samsung_phone.get_cost())
