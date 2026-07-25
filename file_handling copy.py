#is has 4 modes
#read='r'
#write='w'
#append='a'
#create='x'

r=open('new.txt','w')
r.write("This is my first file handling program")
r.close()
print("File written successfully")