# A dataclass is a decorator that automatically generates special methods like __init__(), __repr__(), and __eq__()

# ------------- Without dataclass decorator ---------------------------------
class Point: 
    x: int # this is not an attribute, but a type hint for the x attribute
    y: int = 0

Point(1, 2) # creates a Point object with x=1 and y=2
p = Point() 
p.x  # AttributeError: 'Point' object has no attribute 'x' because the __init__ method is not generated for the Point
p.y  # 0, but it's a class attribute, not an instance attribute. The default value is shared across all instances of the class.

print(p) # <__main__.Point object at 0x7f8b8c8c8c8c> because the __repr__ method is not generated for the Point
Point() == Point() # False, because the __eq__ method is not generated for the Point. 


#---------- With Decorator ----------------------------

@dataclass
class Point: 
    x: int # this is an attribute, and a type hint for the x attribute.
    y: int = 0 # this is an attribute, and a type hint for the y attribute. 

# Python turns that into a the following code: 
class Point: 
    def __init__(self, x: int, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if other.__class__ is not self.__class__: # This checks if the other object is of the same type/class as self. 
            return NotImplemented # special singleton value that indicates that the comparison is not implemented for the given types.
        return self.x == other.x and self.y == other.y # if they are the same class, then compare the attributes x and y for equality.
