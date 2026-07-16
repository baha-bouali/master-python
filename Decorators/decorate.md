# Decorators
A decorator is just a function that takes another function, adds a behavior to it, and returns a new function

Here is a classic function that does only "\"greet"\" 

````python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
````


Now let's make a function call another function and returns it

````python
def my_decorator (funct):
    def wrapper():
        print("Before the func")
        func()
        print("After the func")
    return wrapper

def say_hello():
    print("HELLO")

greet = my_decorator(say_hello)
greet()
````

>> Before the func
>> HELLO
>> After the func

## The '@' syntax (syntactic sugar)

````python
def my_decorator(func):
    def wrapper():
        print("Before the func")
        func()
        print("After the func")
    return wrapper

@my_decorator
def say_hello():
    print("HELLO")

say_hello()
````
>> Before the func
>> HELLO
>> After the func


## Handling Arguments

Real function usually take **arguments**, So the **Wrapper** has to accept and pass them along using `*args, **kwargs`

````python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        
````


