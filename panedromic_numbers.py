a=int(input("Enter a number: "))

if str(a) == str(a)[::-1]:
    print(f"{a} this is an palindromic number")
else:
    print(f"{a} this is not an palindromic number")