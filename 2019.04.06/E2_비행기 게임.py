import sys
sys.stdin = open("E2_비행기 게임_input.txt")

def BFS(x, y):

    queue = []
    queue.append((x, y, 1, 0))

    dx = [-1, -1, -1]
    dy = [-1, 0, 1]

    visited[1][x][y] = 1

    while queue:

        x, y, bomb, score = queue.pop(0)

        for i in range(3):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= 13 or new_y < 0 or new_y >= 5:
                continue
            if new_x == 0:
                if arr[new_x][new_y] == '*':
                    return score + 10
                elif arr[new_x][new_y] == 'X':
                    return score - 7
            if arr[new_x][new_y] == '*':
                visited[bomb][new_x][new_y] = 1
                queue.append((new_x, new_y, bomb, score+10))
            if arr[new_x][new_y] == 'X':
                if bomb == 1:

                    visited[bomb-1][new_x][new_y] = 1
                    queue.append((new_x, new_y, bomb-1, score))
                else:
                    visited[bomb][new_x][new_y] = 1
                    queue.append((new_x, new_y, bomb, score-7))



T = int(input())

for tc in range(T):

    arr = [list(map(str, input())) for _ in range(13)]

    arr2 = [[0 for _ in range(5)] for _ in range(13)]

    for i in range(13):
        for j in range(5):
            arr2[i][j] = arr[i][j]

    # for i in range(13):
    #     print(i, arr[i])

    start_x = 12
    start_y = 2

    visited = [[[0 for _ in range(5)] for _ in range(13)] for _ in range(2)]

    print(BFS(start_x, start_y))

