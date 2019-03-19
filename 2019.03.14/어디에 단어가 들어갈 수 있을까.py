import sys
sys.stdin = open("어디에 단어가 들어갈 수 있을까_input.txt")

T = int(input())

for tc in range(T):

    N, K = map(int, input().split())

    puzzle = []

    for i in range(N):
        puzzle.append(list(map(int, input().split())))

    word = 0

    for i in range(N):
        temp = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                for k in range(N-j):
                    if puzzle[i][j+k] == 1:
                        temp += 1
                
            if temp == K:
                word += 1

    for i in range(N):
        for j in range(N):
            temp = 0
            if puzzle[i][j] == 1:
                for k in range(N-i):
                    if puzzle[i+k][j] == 1:
                        temp += 1
                break
            if temp == K:
                word += 1

    print("#{} {}".format(tc+1, word))





