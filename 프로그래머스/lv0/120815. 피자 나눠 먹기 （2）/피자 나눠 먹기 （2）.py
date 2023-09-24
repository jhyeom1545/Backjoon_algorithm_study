def solution(n):
    if n == 6:
        return 1
    else:
        num = 1
        while True:
            pizza = 6 * num
            if pizza % n == 0:
                break
            else:
                num+=1
        return num
        