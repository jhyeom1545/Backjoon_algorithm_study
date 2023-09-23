def solution(num_list):
    final_num = 0
    final_result = 0
    result_num = 0
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num = num / 2
                result_num += 1
            else:
                num = num - 1
                num = num / 2
                result_num += 1
            if num == 1:
                final_result += result_num
                result_num = 0
                break
        
    return final_result