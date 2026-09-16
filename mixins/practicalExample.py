class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def as_dict(self):
        return {
            "make": self.make,
            "model": self.model
        }
print(Car("Toyota", "Rav4").as_dict()) #{'make': 'Toyota', 'model': 'Rav4'}

# The medhod as_dict() is structurally the same for all classes

# Key idea of a Mixin: Encapsulate a reusable behaviour.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def as_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }
class Car: 
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def as_dict(self):
        return {
            "make": self.make,
            "model": self.model
        }

# See how as_dict is not the same for both classes. We can use a Mixin to encapsulate the behaviour of as_dict() and reuse it in both classes.

# We'll use a Mixin to encapsulate the behaviour of as_dict() in ./mixins/as_dict_mixin.py