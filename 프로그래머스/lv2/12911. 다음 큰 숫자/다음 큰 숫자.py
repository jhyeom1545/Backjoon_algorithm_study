def solution(n):
    c = n+1
    while True:
        if bin(n).count('1') == bin(c).count('1'):
            return c
        c+=1
