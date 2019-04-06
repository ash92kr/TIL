import sys
sys.stdin = open("Magnetic_input.txt")

for tc in range(10):

    N = int(input())

    pan = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for i in range(N):
        for j in range(N):
            flag = 0
            if pan[j][i] == 1:
                for k in range(N-j-1):   # 지금 열이 아니라 +1, +2열부터 검증
                    if pan[j+k+1][i] == 2:
                        flag = 1
                        break
            elif pan[j][i] == 2:
                for k in range(j):
                    if pan[j-k-1][i] == 1:   # 지금 열이 아니라 -1, -2열부터 검증
                        flag = 1
                        break
            if flag == 0:
                pan[j][i] = 0


    flag = 1

    for i in range(N):
        for j in range(N):
            if pan[j][i] == 2 and flag == 1:  # flag가 1 -> 2일 때 count +1
                count += 1
                flag = 2
            elif pan[j][i] == 1:  # flag 2 -> 1일 때는 count하지 않음
                flag = 1


    print("#{} {}".format(tc+1, count))
