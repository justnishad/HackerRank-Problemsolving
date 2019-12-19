#link:https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if(abs(x-z)<abs(y-z)):
        return('Cat A')
    elif(abs(x-z)>abs(y-z)):
        return('Cat B')
    elif(abs(x-z)==abs(y-z)):
        return('Mouse C')


q = int(input())

for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

