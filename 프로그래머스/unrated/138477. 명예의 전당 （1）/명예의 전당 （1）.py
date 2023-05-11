from collections import deque

def solution(k, score):
    answer = []
    a = deque()
    a.append(3) # 처음에 더함
    a.append(2)
    print(a)
    print(a.pop())
    # for i in range(len(score)):
    #     if len(a) == k:
    #         answer.
    #         answer = answer.pop(-1)
    #     else:
    #         answer.insert(0,score[i])
        
        
    return answer
