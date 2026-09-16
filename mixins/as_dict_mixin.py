class asDictMixin:
    def as_dict(self):
        return vars(self)


class Person(asDictMixin):  # This means inherit from asDictMixin in Python.
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Person("baha", 22).as_dict()) #{'name': 'baha', 'age': 22}

class Car(asDictMixin):
    def __init__(self, make, model):
        self.make = make
        self.model = model
print(Car("Toyota", "Hilux").as_dict()) #{'make': 'Toyota', 'model': 'Hilux'}
