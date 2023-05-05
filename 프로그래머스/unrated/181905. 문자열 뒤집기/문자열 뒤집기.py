def solution(my_string, s, e):
    # 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 리턴하는 함수
    
    # 인덱스 s 이전 문자열, 뒤집을 대상 문자열, 인덱스 e 이후 문자열을 각각 분리
    before = my_string[:s]
    target = my_string[s:e+1]
    after = my_string[e+1:]
    
    # 뒤집은 문자열을 구한 후, 세 문자열을 합쳐서 리턴
    reversed_target = target[::-1] # 뒤집기
    return before + reversed_target + after
