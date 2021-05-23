'''
w와 h의 최대공약수가 1일 때 잘리는 박스는 w+h-1개
그렇지 않을 때 잘리는 박스는 w+h-최대공약수 개
'''
def solution(w,h):
    lst = []
    if w == h: return w*h-w
    elif w == 1 or h == 1: return 0

    for i in range(1,w+1):
        if w%i == 0: lst.append(i)
    for i in range(1,h+1):
        if h%i == 0: lst.append(i)

    for i in sorted(lst,reverse=True):
        if lst.count(i) == 2 and i>1:
            return (w*h)-(w+h-i)
        elif lst.count(i) == 2 and i==1:
            return (w*h)-(w+h-1)

w, h = map(int,input().split())
print(solution(w,h))