#link to prob:https://www.hackerrank.com/challenges/bon-appetit/problem
# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    n=len(bill)
    sums=0
    actual=0
    for i in range (n):
        if(i!=k):
            sums=sums+bill[i]
    actual=sums/2
    final=b-actual
    if(final!=0):
        print(int(final))
    else:
        print("Bon Appetit")


nk = input().rstrip().split()

n = int(nk[0])

k = int(nk[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)
