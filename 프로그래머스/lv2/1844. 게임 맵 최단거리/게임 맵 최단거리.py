from collections import deque
# Que 자료구조 사용
def solution(maps):
    answer = 0
    m = len(maps[0]) # 행
    n = len(maps) # 열
    
    visited = [[-1]*m for _ in range(n)] # 방문하지 않은 것으로 모두 표시

    q = deque()
    
    q.append((0, 0))
    visited[0][0] = 1
    
    dx = [0,1,0,-1] # 북, 동, 남, 서
    dy = [1,0,-1,0]
    
    while q:
        x, y = q.popleft() # 제일 앞에서 하나
        
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            # 경기장을 초과하지 않고, maps가 갈 수 있는 곳이고(=1), 이미 간곳이 아님(=-1)
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny)) # 방문한 좌표 까지의 거리
    
    
    return visited[n-1][m-1]