# def solution(s):
#     answer = [-1] * len(s)  # 초기값 -1로 설정

#     prev_char = {}  # 문자별 이전에 등장한 위치를 저장하는 딕셔너리

#     for i in range(len(s)):
#         if s[i] in prev_char:  # 이전에 등장한 문자열이면
#             answer[i] = i - prev_char[s[i]]  # 현재 위치와 이전 위치의 차이를 저장
#         prev_char[s[i]] = i  # 현재 문자열의 위치를 저장

#     return answer
# def solution(s):
#     answer = [-1]*len(s)
#     prev_char = {} # dictionary
    
#     for i in range(len(s)):
#         if s[i] in prev_char:
#             answer[i] = i - prev_char[s[i]]
#         prev_char[s[i]] = i # 현재 문자열 위치 저장
#     print(prev_char)
#     return answer

def solution(s):
    print(s)
    answer = [-1] * len(s)
    char_dict = {} # dictionary 선언
    for i in range(len(s)):
        if s[i] in char_dict:
            answer[i] = i - char_dict[s[i]]
        char_dict[s[i]] = i
    return answer
        