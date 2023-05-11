def solution(lottos, win_nums):
    answer = []
    count= 7
    good_count = 7
    # 모두 0일경우
    if len(lottos) == lottos.count(0):
        answer.append(1)
    else:
        # 최선의 경우
        for i in range(len(win_nums)):
            if lottos[i] in win_nums or lottos[i] == 0:
                good_count -=1
        if good_count == 7:
            good_count = 6
        answer.append(good_count)
        
    # 최악의 경우
    for i in range(len(win_nums)):
        if lottos[i] in win_nums:
            count -=1
    
    print(lottos)
    print(win_nums)
    if count == 7:
        count = 6
    answer.append(count)
    return answer
    