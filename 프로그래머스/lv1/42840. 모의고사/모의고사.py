def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_answer = 0
    second_answer = 0
    third_answer = 0
    for i in range(len(answers)):
        if answers[i] == first[i% len(first)]:
            first_answer+=1
        if answers[i] == second[i% len(second)]:
            second_answer+=1
        if answers[i] == third[i% len(third)]:
            third_answer+=1
    if first_answer == second_answer and third_answer == second_answer:
        return [1, 2, 3]
    elif first_answer == second_answer and second_answer > third_answer:
        return [1, 2]
    elif first_answer == third_answer and third_answer > second_answer:
        return [1, 3]
    elif third_answer == second_answer and third_answer > first_answer:
        return [2, 3]
    elif first_answer > second_answer and first_answer > third_answer:
        return [1]
    elif second_answer > first_answer and second_answer > third_answer:
        return [2]
    elif third_answer > first_answer and third_answer > second_answer:
        return [3]

        
    
    
    