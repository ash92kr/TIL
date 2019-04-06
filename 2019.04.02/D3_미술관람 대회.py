import sys
sys.stdin = open("D3_미술관람 대회_input.txt")

def BFS_blind(x, y, color):

    global count_blind

    queue = []
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:

        x, y = queue.pop(0)

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue
            if pixel_blind[new_x][new_y] != color:
                continue
            pixel_blind[new_x][new_y] = 0
            queue.append((new_x, new_y))

    count_blind += 1


def BFS(x, y, color):

    global count

    queue = []
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:

        x, y = queue.pop(0)

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                continue
            if pixel[new_x][new_y] != color:
                continue
            pixel[new_x][new_y] = 0
            queue.append((new_x, new_y))

    count += 1


N = int(input())

pixel = [list(map(str, input())) for _ in range(N)]
pixel_blind = [[0 for _ in range(N)] for _ in range(N)]   # 깊은 복사

for i in range(N):
    for j in range(N):
        if pixel[i][j] == "G":
            pixel_blind[i][j] = "R"
        else:
            pixel_blind[i][j] = pixel[i][j]

count = 0
count_blind = 0

for i in range(N):
    for j in range(N):
        if pixel[i][j] != 0:
            BFS(i, j, pixel[i][j])

for i in range(N):
    for j in range(N):
        if pixel_blind[i][j] != 0:
            BFS_blind(i, j, pixel_blind[i][j])

print(count, count_blind)
