def solution(quiz):
    last_answer = []
    for answer in quiz:
        my_answer = answer.split(" ")
        a = int(my_answer[0])
        b = my_answer[1]
        c = int(my_answer[2])
        d = int(my_answer[4])
        if b == '-' and a - c == d:
            last_answer.append("O")
        elif b == '+' and a + c == d:
            last_answer.append("O")
        else:
            last_answer.append("X")
            
    return last_answer