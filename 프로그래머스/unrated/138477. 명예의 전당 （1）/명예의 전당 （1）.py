def solution(k, score):
    answer = []  # 정답 리스트
    a=[]  # 1등 후보 리스트
    for i in score:  # score 리스트의 요소를 하나씩 탐색
        if len(a)<k:  # a 리스트에 저장된 수가 k개 이하이면
            a.append(i)  # a 리스트에 해당 요소 추가
        else:  # a 리스트에 저장된 수가 k개 이상이면
            if min(a)<i:  # a 리스트에 저장된 수 중 가장 작은 수보다 i가 크다면
                a.remove(min(a))  # a 리스트에서 가장 작은 수 삭제
                a.append(i)  # a 리스트에 해당 요소 추가
        answer.append(min(a))  # 현재까지 a 리스트에서 가장 작은 수 추가
    return answer  # 정답 리스트 반환
