class PhonePrototype(object):
    def __init__(self, value='default'):
        self.value = value

    def set_value(self, value):
        self.value = value

    def clone(self):
        obj = self.__class__()
        obj.__dict__.update(value=self.value)
        return obj


class PhonePrototypeManager(object):
    def __init__(self):
        self.phones = {}

    def add_phone(self, name, phone):
        self.phones[name] = phone

    def remove_phone(self, name):
        del self.phones[name]

    def get_phones(self):
        print([{n: p.value} for n, p in self.phones.items()])


if __name__ == '__main__':
    manager = PhonePrototypeManager()
    phone = PhonePrototype()
    manager.add_phone('default phone', phone.clone())
    phone.set_value('apple')
    manager.add_phone('apple phone', phone.clone())
    phone.set_value('samsung')
    manager.add_phone('samsung phone', phone.clone())
    manager.get_phones()
