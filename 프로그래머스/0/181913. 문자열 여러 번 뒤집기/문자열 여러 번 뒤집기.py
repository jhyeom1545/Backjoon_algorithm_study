def solution(my_string, queries):
    new_str = my_string
    for q in queries:
        start = q[0]
        end = q[1]+1
        change = new_str[start:end][::-1]
        new_str = new_str[:start] + change + new_str[end:]
    return new_str