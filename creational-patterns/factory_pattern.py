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


class Company(ABC):
    def get_phone(self):
        return self.phone_factory()

    @abstractmethod
    def phone_factory(self):
        pass


class AppleCompany(Company):
    def phone_factory(self):
        return ApplePhone()


class SamsungCompany(Company):
    def phone_factory(self):
        return SamsungPhone()


if __name__ == '__main__':
    apple_company = AppleCompany()
    apple_company.get_phone().name()

    samsung_company = SamsungCompany()
    samsung_company.get_phone().name()
