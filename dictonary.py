#Dictionary is a collection of key and value pairs.

d={30:300,40:400,50:500}

d.update({60:600,70:700}) #adding key and value by using the update method
d[80]=800   #creating key and value by using the assignment operator
del d[30]  #removing key and value by using the del method


print(d)

help(dict)