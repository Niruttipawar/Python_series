#syntax error

'''print("Hello, World!"'''

#indentation error

'''a=5
if a>2:
print("a is greater than 2")'''  #the print statement is not if statement block

# tab error

'''            print("Hello, World!")  #the print statement is not properly indented'''

#exception error

'''print("start")
print(10/0) #this line throw exception error
print("end")  #this line will not run'''



#exception handling
#try 
#exeption
#finally

'''a=int(input("Enter the number :-"))
try:
    print(10/a)

except Exception as err:
    print(f"Error is :- {err}")

finally:
    print("This line will always run")
'''
age=int(input("Enter the age :-"))

if age > 18 or age < 10:
    raise ValueError("Age is not valid")
else:
    print("Age is valid")

    