# def solution(str_list):
#     answer = []
#     for i in range(len(str_list)):
#         if str_list[i]=="l":
#             return str_list[:i]
#         if str_list[i]=="r":
#             return str_list[i:]
#     return []

def solution(str_list):
    left = []
    right = []
    for s in str_list:
        if s == 'l':
            return left
        elif s == 'r':
            return str_list[len(left) + 1:]
        else:
            left.append(s)
    return []