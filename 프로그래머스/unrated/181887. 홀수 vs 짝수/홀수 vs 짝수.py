def solution(num_list):
    odd = 0 # 홀수
    even = 0 # 짝수
    result = 0
    
    for i in range(len(num_list)):
        if (i+1) % 2 == 0:
            even += num_list[i]
        else:
            odd += num_list[i]
    if even >= odd:
        result = even
    else:
        result = odd
    return result