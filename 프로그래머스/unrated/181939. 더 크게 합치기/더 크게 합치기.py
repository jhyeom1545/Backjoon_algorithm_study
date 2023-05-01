def solution(a, b):
    left = str(a) + str(b)
    right = str(b) + str(a)
    return int(left) if  int(left) >= int(right) else int(right)