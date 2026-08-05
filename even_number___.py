# Program to print even numbers between two values
# Input values
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Even numbers between {start} and {end} are:")

# Using a for loop
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")
