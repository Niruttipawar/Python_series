#khat song loop
import time
a = ("teri baate na samaj si lag rhi hai..\n"
",tuu preshan kr rhi hai,..tere liye mandir jau,\n"
" tere naam ka diya jalau,..tere liye mandir jau,\n"
" tere naam ka diya jalau,....")

for i in range(0, 1):  # Loop 5 times
    print("Iteration:", i , ":", a)
    time.sleep(2)  # pauses for 1 second

print(a)