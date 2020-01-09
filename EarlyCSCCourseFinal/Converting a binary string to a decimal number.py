#converting Binary

binary= input("Please input a binary number")

n= len(binary)-1



total=0


for x in range (len(binary)):
    if binary[x]=='1':
        total+= 2**n
    n=n-1
print(total)
