# A generator is a function that returns an iterator. 
# It allows you to declare a function that behaves like an iterator, 
# i.e., it can be used in a for loop. 


# Example
ids = (n for n in [1, 2, 3])
print ("first read: ", list(ids)) # [1, 2, 3]
print("second read: ", list(ids)) # This will return an empty list because the generator has already been exhausted.


ids = [n for n in [7]]          # SQUARE brackets
print("first read: ", list(ids))   # [7]
print("second read:", list(ids))   # [7]



# Falsy and Truthy values
# In Python, values can be evaluated in a boolean context, meaning they can be considered either "truthy" or "falsy."

empty = (n for n in [])
print (bool(empty))  # True, an empty generator is still True because it is an object that can be iterated over, even if it yields no values.
print(bool(([]))) # False, an empty list is considered false because it has no values. 