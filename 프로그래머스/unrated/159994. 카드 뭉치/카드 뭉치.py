# def solution(cards1, cards2, goal):
#     answer = 'Yes'
    
#     # 현재까지 각 덱에서 맞춘 카드의 인덱스를 초기화합니다.
#     card1_idx, card2_idx = 0, 0
    
#     # goal 문자열에 대해 반복문을 돌면서 두 덱에서 카드를 꺼내 비교합니다.
#     for word in goal:
#         # cards1 덱에서 현재 위치의 카드가 goal 문자열과 같은 경우,
#         # card1_idx를 증가시켜서 다음 카드를 가리키게 합니다.
#         if len(cards1) > card1_idx and word == cards1[card1_idx]:
#             card1_idx += 1
#         # cards2 덱에서 현재 위치의 카드가 goal 문자열과 같은 경우,
#         # card2_idx를 증가시켜서 다음 카드를 가리키게 합니다.
#         elif len(cards2) > card2_idx and word == cards2[card2_idx]:
#             card2_idx += 1
#         # 현재 문자가 두 덱에서 모두 찾을 수 없는 문자인 경우,
#         # answer 변수를 'No'로 바꾸고 반복문을 종료합니다.
#         else:
#             answer = "No"
#             break
    
#     # 결과값을 반환합니다.
#     return answer

def solution(cards1, cards2, goal):
    answer = "Yes"
    card1_idx, card2_idx = 0, 0
    for word in goal:
        if len(cards1) > card1_idx and word == cards1[card1_idx]:
            card1_idx+=1
        elif len(cards2) > card2_idx and word == cards2[card2_idx]:
            card2_idx+=1
        else:
            return "No"
    return answer