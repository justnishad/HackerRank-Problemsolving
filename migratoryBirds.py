#link to problem:https://www.hackerrank.com/challenges/migratory-birds/problem
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    n=len(arr)
    second=[]
    third=[]
    for i in range(n):
        temp=arr[i]
        if(temp not in second):
            second.append(temp)
    second.sort()
    m=len(second)
    for j in range(m):
        third.append(arr.count(second[j]))
    x=third.index(max(third))
    return(second[x])
    


arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

