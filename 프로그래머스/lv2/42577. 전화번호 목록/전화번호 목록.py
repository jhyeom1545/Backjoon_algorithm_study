def solution(phone_book):
    answer = True
    phone_book.sort()  # 전화번호를 사전순으로 정렬합니다.
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return answer
