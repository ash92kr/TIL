import sys
sys.stdin = open("스도쿠 검증_input.txt")

T = int(input())

for tc in range(T):

    flag = 1

    scoku = []

    for i in range(9):
        scoku.append(list(map(int, input().split())))

    for i in range(len(scoku)):   # 세로 방향 검증(0행 기준으로 아래로 내려감)
        num = []
        for j in range(len(scoku)):
            if scoku[0+j][i] not in num:
                num.append(scoku[0+j][i])
            else:
                flag = 0
                break

    for i in range(len(scoku)):   # 가로 방향 검증(0열 기준으로 오른쪽으로 감)
        num = []
        for j in range(len(scoku)):
            if scoku[i][0+j] not in num:
                num.append(scoku[i][0+j])
            else:
                flag = 0
                break

    for i in range(0, len(scoku), 3):   # 행렬 검증(3단위씩 건너뜀)
        for j in range(0, len(scoku), 3):
            num = []
            for k in range(3):
                if scoku[i+k][j+k] not in num:
                    num.append(scoku[i+k][j+k])
                else:
                    flag = 0
                    break

    print("#{} {}".format(tc+1, flag))
