import sys
sys.stdin = open("농작물 수확하기_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    data = [list(map(int, input())) for _ in range(N)]

    rice = 0

    start = N//2
    end = N//2

    for i in range(N):
        if i < (N//2):
            for j in range(start, end+1):
                rice += data[i][j]
            start -= 1
            end += 1
        elif i == N//2:   # 절반 지점이 되었는데 start와 end를 계속 빼면 음수가 나옴
            for j in range(N):
                rice += data[i][j]
        else:
            start += 1
            end -= 1
            for j in range(start, end+1):
                rice += data[i][j]


    print("#{} {}".format(tc+1, rice))