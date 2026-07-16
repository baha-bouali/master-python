# A function that takes a function

def loud(func):
    print("About to run somthing")
    func()
    print("Job Done")

def greet():
    print("Doing Job ....")

# greet = loud(greet)
# greet()


#-------------------------------------------------
# A function that returns a function 

def make_loud(func):
    def wrapper():
        print("About to do something")
        func()
        print("Done")

    return wrapper  # Returns the function itself, not calls it

def new_greeting():
    print("Greets... ")

# new_greet = make_loud(new_greeting)
# new_greet()

#---------------------------------------------------------

# A decorator, but with ugly syntax 
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("HELLO")

say_hello()