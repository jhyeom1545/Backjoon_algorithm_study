def solution(a, b, n):
    count = 0
    empty = n
    while empty >= a:
        # a개의 빈 병을 받을 때 필요한 콜라 개수 계산
        need = (empty // a) * b
        # 총 콜라 개수 누적
        count += need
        # 받은 콜라 개수만큼 빈 병 추가
        empty = (empty % a) + need
    return count
