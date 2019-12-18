#link to problem:https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count=0
    l=[]
    for i in range(0,n):
        l.append(ar[i])
    for i in range(0,n):
        for j in range(0,n):
            if(i<j):
                 x=ar[i]+l[j]
                 if(x%k==0):
                     count=count+1
    return(count)           


nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(result)