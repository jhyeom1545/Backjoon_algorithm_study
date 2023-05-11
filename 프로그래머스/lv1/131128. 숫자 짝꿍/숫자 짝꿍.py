# def solution(X, Y):
#     answer = ''

#     # 9부터 0까지 각 숫자에 대해, 해당 숫자가 X와 Y 두 문자열에 몇 번 나타나는지 확인하여
#     # 더 적게 나타나는 횟수만큼, answer 문자열에 해당 숫자를 추가합니다.
#     # 이를 통해 두 문자열에 공통적으로 포함된 숫자들만 answer에 추가됩니다.
#     for i in range(9,-1,-1) :
#         answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
#         # 9부터 추가했기 때문에 무조건 큰수가 변환되겠네요

# #     # answer가 비어있으면 X와 Y에 공통으로 포함된 숫자가 없다는 의미이므로 '-1'을 반환합니다.
#     if answer == '' :
#         return '-1'
# #     # answer가 '0'으로만 이루어져 있으면, answer에 포함된 숫자들이 모두 0이라는 의미이므로 '0'을 반환합니다.
#     elif len(answer) == answer.count('0'):
#         return '0'
#     # 그 외의 경우에는 answer를 반환합니다.
#     else :
#         return answer

def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        answer+= str(i) * min(X.count(str(i)), Y.count(str(i)))
    if answer == '':
        return "-1"
    if len(answer) == answer.count('0'):
        return "0"
    return answer
    