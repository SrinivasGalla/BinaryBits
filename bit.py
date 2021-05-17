'''
#to check whether the give position is set or not
num=16
p=3
if num&((p-1)<<1): #Here it will left shift the one and it will compare with num
    print("YES")#if the given position is set
else:
    print("NO")#if the position is not set
'''
'''
#to count the set bits in a number
num=int(input( "enter the number :"))
c=0
while num!=0: # here we checking num greater o1 or not
    if (num&1==1): #here we comparing number with 1
        c+=1
    num=num>>1 #it left shift the number
print(c)

'''
#convert the set to unset

n=int(input("Enter the number : "))
p=3
x=n^((p-1)<<1)
print(x)