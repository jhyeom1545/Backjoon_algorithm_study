def solution(numbers, direction):
    if direction == "left":
        one = numbers.pop(0)
        numbers.append(one)
    else:
        one = numbers.pop(-1)
        numbers.insert(0, one)
    return numbers