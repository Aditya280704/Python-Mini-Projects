# BY USING * WE CAN PASS ANY NUMBER OF ARGUMENTS
def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

print(add(2, 3, 4 ))


def calculate(n, **kwargs):
    # created unlimited keyword argument
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
# n is now predefined and kwargs is rest of dictionary

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan",model="Skyline")
print(my_car.make)

