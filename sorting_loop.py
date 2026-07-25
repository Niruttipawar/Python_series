a = [11, 12, 13, 14]

for i in range(len(a) - 1):  # stop at second-to-last index
    if a[i] < a[i+1]:
        continue
    else:
        print("this is not a sorted list")
        break
else:
    print("this is a sorted list")
