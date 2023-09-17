def solution(myString):
    answer = []
    new_answer = []
    
    answer = myString.split("x")
    for i in answer:
        if i != '':
            new_answer.append(i)
    new_answer.sort()
    return new_answer