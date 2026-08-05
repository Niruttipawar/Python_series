# here we do the read opretion by using read 'r' opreation

'''file = open("diary.txt")
print(file.read())
file.close()'''

# here we do the write opretion by using write 'w' opretion of file handling

'''file = open("diary.txt",'w')
file.write("this an my first file I'll created :")
print(file)
file.close()'''

#here we do the append opretion by using 'a'

'''file = open("diary.txt",'a')
file.write("this an my second file I'll created :")
print(file)
file.close()
'''

# the readlines is we you read the specific one line of an file :
file = open("diary.txt",'r')
print(file.readlines())
file.close()