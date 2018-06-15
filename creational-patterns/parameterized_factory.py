from abc import ABC, abstractmethod


class Phone(ABC):
    @abstractmethod
    def name(self):
        pass


class ApplePhone(Phone):
    def name(self):
        print('apple phone')


class SamsungPhone(Phone):
    def name(self):
        print('samsung phone')


class Company():
    def get_phone(self, cls):
        return self.phone_factory(cls)

    def phone_factory(self, cls):
        return cls()


if __name__ == '__main__':
    company = Company()
    company.get_phone(ApplePhone).name()
    company.get_phone(SamsungPhone).name()
