import sys
sys.stdin = open("달팽이 숫자_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    array = [[0 for _ in range(N)] for _ in range(N)]

    number = 0
    x = 0
    y = -1
    idx = N

    while idx >= 1:  # 더 이상 반복할 횟수가 없을 때까지 실시

        for i in range(idx):  # 오른쪽(열 추가)
            y += 1
            number += 1
            array[x][y] = number
        idx -= 1

        for i in range(idx):  # 아래쪽(행 추가)
            x += 1
            number += 1
            array[x][y] = number

        for i in range(idx):  # 왼쪽(열 감소)
            y -= 1
            number += 1
            array[x][y] = number
        idx -= 1

        for i in range(idx):  # 위쪽(행 감소)
            x -= 1
            number += 1
            array[x][y] = number
    
    # 출력
    print("#{}".format(tc+1))
    for i in range(N):
        for j in range(N):
            print("{}".format(array[i][j]), end=" ")
        print()





