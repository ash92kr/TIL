import sys
sys.stdin = open("B7_로봇 과자 먹기_input.txt")

def DFS(number, count, temp):

    global min_hab

    if temp > min_hab:
        return

    if number == N:
        if temp < min_hab:
            min_hab = temp
            return min_hab
        return

    for i in range(N):
        if check[i]:
            continue
        record[i] = all_distance[count][i]
        check[i] = 1
        DFS(number+1, count+1, temp+record[i])
        check[i] = 0



def BFS(x, y):

    global end_x, end_y

    queue = []
    queue.append((x, y, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0 for _ in range(101)] for _ in range(101)]
    visited[x][y] = 1

    while queue:

        x, y, count = queue.pop(0)

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x >= 101 or new_y < 0 or new_y >= 101:
                continue
            if visited[new_x][new_y] == 1:
                continue
            if new_x == end_x and new_y == end_y:
                return count + 1
            visited[new_x][new_y] = 1
            queue.append((new_x, new_y, count + 1))

    return -1


T = int(input())

for tc in range(T):

    N = int(input())

    cookie = list(map(int, input().split()))
    robot = list(map(int, input().split()))

    all_distance = []

    for i in range(0, len(robot), 2):
        temp = []
        for j in range(0, len(cookie), 2):
            end_x = cookie[j]
            end_y = cookie[j+1]
            temp.append(BFS(robot[i], robot[i+1]))
        all_distance.append(temp)


    record = [0] * N
    check = [0] * N
    min_hab = 987654321

    DFS(0, 0, 0)

    # print("#{} {}".format(tc+1, min_hab))
    print(min_hab)