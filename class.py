
"""" Private method we can not access the private variable outside the class
 but we can access it by using getter method"""


class app:

    def __init__(self,name,password):
        self.name = name
        self.__password = password  #private variable

    def get_password(self):
        return self.__password

    print(get_password)  # Give error because it is private

s1=app("Nivrutti","1234")
print(s1.name)
print(s1.get_password())  












"""class car: #class decration 
    colour= "black"
    model= "BMW"
    engine= "V8"

car1 = car()  #the S1 is an object of class

print(car1.colour) # it displays the data of car class 
print(car1.model) # it displays the data of car class 
print(car1.engine) # it displays the data of car class 

"""

