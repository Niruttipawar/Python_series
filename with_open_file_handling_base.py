#read opreation using with open() function  

with open('hello.txt', 'r') as p:
    print(p.read())

#write operation using with open() function

'''with open('hello.txt', 'w') as p:
    p.write("Hello, World!")
print("File created successfully")'''

#update operation using with open() function using functions
"""with open('hello.txt', 'a') as p:
    for i in range(5):
        p.write("\nHello, World!")"""