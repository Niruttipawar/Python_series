salary=int(input("Enter the salary :-"))

if salary < 30000:
    print(f"the final tax is of 5% is :- {salary*5/100}")


if salary > 70000:
    print(f"the final tax of 25% is :- {salary*25/100}")


else:
    print(f"the final tax of 15% is :- {salary*15/100}")



