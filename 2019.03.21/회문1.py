import sys
sys.stdin = open("회문1_input.txt")

for tc in range(10):

    N = int(input())

    arr = [list(map(str, input())) for i in range(8)]

    pal = 0

    # 가로
    for i in range(8):
        for j in range(8-N+1):
            flag = 1
            for k in range(N//2):
                if arr[i][j+k] != arr[i][j+N-1-k]:
                    flag = 0
                    break
            if flag:
                pal += 1

    # 세로
    for i in range(8):
        for j in range(8-N+1):
            flag = 1
            for k in range(N//2):
                if arr[j+k][i] != arr[j+N-1-k][i]:
                    flag = 0
            if flag:
                pal += 1

    print("#{} {}".format(tc+1, pal))
