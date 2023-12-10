def solution(order):
    answer = 0
    for preorder in order:
        if 'americano' in preorder:
            answer += 4500
        elif 'cafelatte' in preorder:
            answer += 5000
        else:
            answer += 4500
    return answer