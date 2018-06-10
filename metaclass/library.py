
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print(cls)


class Base(metaclass=BaseMeta):
    pass