def solution(food):
    answer = [0]
    num = 1
    first, second = [], []
    for i in range(1, len(food)):
        if food[i] % 2 == 1:
            food[i] = food[i]-1
        for j in range(food[i]//2):
            first.append(str(num))
            second.insert(0,str(num))
        num+=1
    first.append(str(0))
    result = "".join(first)
    second = "".join(second)
    return result + second