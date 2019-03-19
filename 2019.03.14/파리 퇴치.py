import sys
sys.stdin = open("파리 퇴치_input.txt")

T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    array = []

    for i in range(N):
        array.append(list(map(int, input().split())))

    fly = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += array[i+k][j+l]
            if fly < temp:
                fly = temp

    print("#{} {}".format(tc+1, fly))



