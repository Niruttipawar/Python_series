d={30:300,40:400,50:500}
d1={30:300,40:600,50:500}

print(d.items())
print(d.keys())

for i in d:
    if i in d.keys():
        d[i] += d1[i]
    else:
        d[i] = d1[i]




