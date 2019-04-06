import sys
sys.stdin = open("E5_암소 미인 대회_input.txt")


def DFS():

    global N, M, count

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()   # 처음 스택에는 하나의 좌표만 들어감

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue
            if data[new_x][new_y] != 'X':  # 새로운 좌표가 X여야 이동 가능
                continue
            data[new_x][new_y] = count  # 하나의 점에 있는 모든 X 좌표를 숫자로 변경
            stack.append((new_x, new_y))


def BFS():

    global N, M

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:

        x, y = queue.pop(0)

        if data[x][y] == 2:   # 2번 좌표에 도달할 경우
            return visited[x][y] - 1   # 현재 좌표의 visited에서 1을 제외해야 한다

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue
            if visited[new_x][new_y] > visited[x][y] + 1:  # 최단 거리로 변경하기
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y))


N, M = map(int, input().split())

data = [list(map(str, input())) for _ in range(N)]
visited = [[987654321 for _ in range(M)] for _ in range(N)]   # 점과 점 사이의 최단 거리

count = 0

for i in range(N):
    for j in range(M):
        if data[i][j] == "X":   # X인 좌표를 찾으면 count를 1 증가시키고 연결된 모든 점들을 해당 숫자로 변경함
            count += 1
            data[i][j] = count
            stack = []   # 스택에 처음으로 X인 좌표를 넣음 -> 연결된 모든 점을 count로 변경
            stack.append((i, j))
            DFS()

queue = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:   # 1번 점의 모든 좌표가 큐에 들어감 -> 그 지역의 모든 최단 거리는 0이 된다
            queue.append((i, j))
            visited[i][j] = 0

print(BFS())

