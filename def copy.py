
#positional arguments

'''def sum(a, b):
    print("The sum of", a, "and", b, "is:", a + b)

sum(5, 10)
'''

#keyword arguments
'''def sum(name,rollno):
    print(f"The name is {name} and the rollno is {rollno}")


sum(name="Alice", rollno=10)
'''


#default arguments
from os import name


def sum(a,b=10):
    print(f"The a is {a} and the b is {b} the sum is {a+b}")


sum(a=12,)
