import sys
sys.stdin = open("어디에 단어가 들어갈 수 있을까_input.txt")

T = int(input())

for tc in range(T):

    N, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    # for i in range(N):
    #     print(data[i])

    count = 0

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                for k in range(N-j):
                    visited[j][j+k] = 1
        temp = 0
        for i in range(N):
            if visited[i] == 1:

        if temp == K:
            count += 1

    # for i in range(N):
    #     for j in range(N):
    #         visited = [0] * N
    #         for k in range(N-1-i):
    #             if data[j][i+k] == 1:
    #                visited[i+k] = 1
    #         if sum(visited) == K:
    #             count += 1

    print("#{} {}".format(tc+1, count))
