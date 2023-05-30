# *args - add multiple arguments
# args is a tuple
def add(*args):
    print(type(args))
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum



add(3,4,5,6,7,8)

# kwargs - keyword argument
# kwargs is a dictionary
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mul"]
    return n


print(calculate(2, add=3, mul=5))

class Car():
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

# will crash since model not specified in optional arguments - use get() method to avoid this
my_car = Car(make="Nissan")

# will return None since model not specified
print(my_car.model)
