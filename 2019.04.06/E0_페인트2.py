import sys
sys.stdin = open("E0_페인트2_input.txt")

def DFS(depth, count):   # 중복없는 조합

    global max_change, visited

    if depth >= 2:
        if count == 2:
            # for i in range(2):
            #     print(record[i])
            # print()
            temp = 0
            visited = [[0 for _ in range(N)] for _ in range(N)]   # visited 체크는 잉크 2번 모두 떨어트린 다음에 초기화해야 한다

            for i in range(2):
                temp += BFS(record[i])
            # temp = BFS(record[0], record[1])
            if temp > max_change:
                max_change = temp
                print(record[0], record[1])
            return

    for i in range(len(start)):
        if check[i]:
            continue
        record[depth] = start[i]
        check[i] = 1
        DFS(depth+1, count+1)
        check[i] = 0


def BFS(point):

    global visited

    queue = []
    queue.append((point[0], point[1], point[2]))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ink = 0

    if arr[point[0]][point[1]] == 0 and visited[point[0]][point[1]] == 0:   # 시작점이 잉크가 없고 방문한 적 없다면 +1
        ink += 1
    visited[point[0]][point[1]] = 1   # 시작점 방문 체크

    while queue:

        x, y, count = queue.pop(0)

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue
            if visited[new_x][new_y] == 1:
                continue
            if count == M:
                continue

            visited[new_x][new_y] = 1
            if arr[new_x][new_y] == 0:
                ink += 1
            queue.append((new_x, new_y, count+1))

    return ink

N = int(input())

M = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]  # visited 체크는 2번 모두 떨어트린 다음에 초기화해야 한다

start = []

for i in range(N):
    for j in range(N):
        start.append((i, j, 0))   # 모든 출발 좌표를 넣어야 한다

record = [0] * 2
check = [0] * (len(start))

max_change = 0

DFS(0, 0)

print(max_change)