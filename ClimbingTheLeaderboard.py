#!/bin/python3

import math
import os
import random
import re
import sys
#link to prob:https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#partially correct fails on large data as not optimized help if u can
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    c=1
    sl=[]
    f=[]
    n=len(alice)
    for i in range (n):
        scores.append(alice[i])
        scores.sort(reverse=True)
        for j in range(len(scores)):
           sl.append(c)
           if(j!=len(scores)-1):
              if(scores[j+1]!=scores[j]):
                c=c+1
        
        f.append(sl[scores.index(alice[i])])    
    return f
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
