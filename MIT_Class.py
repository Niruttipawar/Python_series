class student:
    collagename = "MIT College"

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

print(student.collagename)
S1 = student("Nivrutti", 16)
print(S1.name, S1.rollno)

S2 = student("Siddhanth", 6)
print(S2.name, S2.rollno)




"""
@staticmethod     # is use to covert the function into static method'''
def hello():
    print("Hello Nivrutti")

"""



