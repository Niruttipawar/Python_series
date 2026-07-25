a=int(input("Enter a number: "))
copy=a
rev=0


while a>0:
    rev=rev * 10 + a % 10
    a=a//10

if copy==rev:
    print("The number is a palindrome")

else:
    print("The number is not a palindrome")