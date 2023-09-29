def solution(s):
    answer = []
    answer_dic = {}
    for i in s:
        if i not in answer_dic.keys():
            answer_dic[i] = 1
        elif i in answer_dic.keys():
            answer_dic[i] = answer_dic[i] + 1
    for key_, value_ in answer_dic.items():
        if value_ == 1:
            answer.append(key_)
    answer.sort()
    return ''.join(answer)