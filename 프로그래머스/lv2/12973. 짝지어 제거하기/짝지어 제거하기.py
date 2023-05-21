def solution(s):
    # 홀수개면 수행 못함
    word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if len(s)%2==1:
        return 0
    for i in word:
        if s.count(i) % 2 == 1:
            return 0
    if len(s) % 2 == 1: return 0 # 문자가 홀수개면 무조건 남는다.
    if len(s) == 2: # 문자가 2개이고, 같은 문자라면 무조건 가능
        return 1 if s[0] == s[1] else 0
            
    stack = [s[0]]
    
    for v in s[1:]:
        if len(stack) > 0 and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
            
    return 0 if len(stack) else 1