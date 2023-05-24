def solution(n, computers):
    answer = 0
    visited = [0] * n  # 방문 여부를 저장하는 리스트 초기화

    def dfs(computers, visited, start):
        stack = [start] # 0으로 시작
        while stack: # stack에 뭔가 있으면 while
            j = stack.pop() # 하나 뽑음
            if visited[j] == 0: # 방문 하지 않았으면
                visited[j] = 1 # 방문으로 변경
            for i in range(len(computers)): # computers의 len 만큼 반복문
                if computers[j][i] == 1 and visited[i] == 0: # computers[0][0]== 1이면 and visited[i] 방문 하지 않았으면 append 마지막에 하나 더하기
                    stack.append(i)

    for i in range(n):
        if visited[i] == 0: # false
            dfs(computers, visited, i)
            answer += 1

    return answer
