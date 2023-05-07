def solution(sizes):
    솔트 = []
    가로 = 0
    세로 = 0
    for i in range(len(sizes)):
        my = sizes[i]
        my.sort()
        솔트.append(my)
    for i in range(len(sizes)):
        if 가로 < 솔트[i][0]: 가로 = 솔트[i][0]
        if 세로 < 솔트[i][1]: 세로 = 솔트[i][1]
    return 가로 * 세로
        
    
    