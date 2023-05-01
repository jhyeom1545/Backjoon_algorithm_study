def solution(a, b):
    A = str(a) + str(b)
    B = 2 * a * b
    return int(A) if int(A) >= B else B