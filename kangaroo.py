#Kangaroo
#You are choreograhing a circus show with various animals. For one act, you are given two kangaroos on a
#number line ready to jump in the positive direction (i.e, toward positive infinity).
#The first kangaroo starts at location and moves at a rate of meters per jump.
#The second kangaroo starts at location and moves at a rate of meters per jump.
#You have to figure out a way to get both kangaroos at the same location as part of the show.
#Complete the function kangaroo which takes starting location and speed of both kangaroos as input, and
#return or appropriately. Can you determine if the kangaroos will ever land at the same location
#at the same time? The two kangaroos must land at the same location after making the same number of
#jumps.
#Input Format
#A single line of four space-separated integers denoting the respective values of , , , and .
#Constraints
#Output Format
#Print YES if they can land on the same location at the same time; otherwise, print NO .
#Note: The two kangaroos must land at the same location after making the same number of jumps .
#Sample Input 0
#0 3 4 2
#Sample Output 0
#YES

x1=int(input('Position of kangaroo 1\n'))
v1=int(input('Speed of kangaroo 1\n'))
x2=int(input('Position of kangaroo 2\n'))
v2=int(input('Speed of kangaroo 2\n'))
temp=0
z=0
while(z!=100000):
    x1=x1+v1
    x2=x2+v2
    z=z+1
    if(x1==x2):
        temp=1
        break

if(temp==1):
    print('yes')
else:
    print('no')