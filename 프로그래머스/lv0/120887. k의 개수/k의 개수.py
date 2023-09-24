def solution(i, j, k):
    result = 0
    for idx in range(i, j+1):
        for num in str(idx):
            if int(num) == k:
                result+=1
    return result