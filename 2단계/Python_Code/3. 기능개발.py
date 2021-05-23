import sys
from collections import defaultdict

p = list(map(int,sys.stdin.readline().split()))
s = list(map(int,sys.stdin.readline().split()))

def solution(progresses, speeds):
    pass_lst = [0]*len(progresses)
    count, answer = defaultdict(int), []

    for i in range(len(progresses)):
        for t in range(1,100):
            if progresses[i] + (speeds[i]*t) >= 100:
                if pass_lst[i-1]> t: pass_lst[i] = pass_lst[i-1]
                else: pass_lst[i] = t
                count[pass_lst[i]] += 1
                break

    for v in count.values(): answer.append(v)
    return answer

print(solution(p,s))