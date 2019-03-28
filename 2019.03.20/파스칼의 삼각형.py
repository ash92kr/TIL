import sys
sys.stdin = open("파스칼의 삼각형_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    pascal = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if j == 0:
                pascal[i][j] = 1
            elif j == N-1:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print("#{}".format(tc+1))
    for k in range(N):
        for l in range(N):
            if pascal[k][l] != 0:
                print(pascal[k][l], end=" ")
        print()




