def solution(price, money, count):
    result = 0
    for i in range(1,count+1):
        result += price * i
    return 0 if result - money < 0 else result - money
