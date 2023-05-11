def solution(N, stages):
    # N: 전체 스테이지의 수
    # stages: 사용자가 현재 멈춰있는 스테이지의 번호 배열
                               
    # 스테이지에 도달한 사람의 수
    people = len(stages)
    # 스테이지별 실패율을 담을 딕셔너리
    fail_list = {}
    # N개의 스테이지에 대해 반복
    for i in range(1, N + 1):
        # 아직 도달하지 못한 사람이 있으면
        if people != 0:
            # 해당 스테이지에 머물러 있는 플레이어 수 / 스테이지에 도달한 플레이어 수
            fail_list[i] = stages.count(i) / people
            # 이번 스테이지에 도달한 사람의 수를 차감
            people -= stages.count(i)
        # 모든 플레이어가 스테이지를 통과했으면
        else:
            # 해당 스테이지의 실패율을 0으로 설정
            fail_list[i] = 0
    # 실패율을 기준으로 딕셔너리를 정렬하여 실패율이 높은 스테이지부터 리턴
    return sorted(fail_list, key=lambda i: fail_list[i], reverse=True)
