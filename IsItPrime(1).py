#Casey Wenner
#Homework4
#Is it prime?
import math
x= int(input("Enter a positive integer: "))
count = x-1
Nprime=0
while count > 1:
    if(x%count)==0:
        Nprime=Nprime+1
    count=count-1
if Nprime > 0:
    print("No, ", x," is not prime.")
else:
    print("Yes, ", x," is  prime.")
