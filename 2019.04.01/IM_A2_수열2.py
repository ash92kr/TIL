import sys
sys.stdin = open("IM_A2_수열2_input.txt")

N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

count = 0

# 왼쪽에서 오른쪽으로
for i in range(N):
    for j in range(N):
        temp = 1   # 시작점도 연속되는 배열의 개수로 포함해야 한다
        start = data[i][j]
        for k in range(1, N-j-1):  # 오른쪽으로 갈수록 반복 횟수가 줄어든다
            if start + k == data[i][j+k]:
                temp += 1
            elif start - k == data[i][j+k]:  # 감소 or 증가 어느 한쪽만 반복된다
                temp += 1
            else:
                break  # 한번이라도 순차증감에서 벗어나면 반복문 벗어난다
        if temp > count:
            count = temp

# 오른쪽에서 왼쪽으로
for i in range(N):
    for j in range(N-1, -1, -1):
        temp = 1
        start = data[i][j]
        for k in range(1, j+1):  # 3 -> 3번, 2 -> 2번, 1 -> 1번, 0 -> 0번 반복
            if start + k == data[i][j-k]:
                temp += 1
            elif start - k == data[i][j-k]:
                temp += 1
            else:
                break
        if temp > count:
            count = temp

# 위에서 아래로
for i in range(N):
    for j in range(N):
        temp = 1
        start = data[j][i]
        for k in range(1, N-j-1):
            if start + k == data[j+k][i]:
                temp += 1
            elif start - k == data[j+k][i]:
                temp += 1
            else:
                break
        if temp > count:
            count = temp

# 아래에서 위로
for i in range(N):
    for j in range(N-1, -1, -1):
        temp = 1
        start = data[j][i]
        for k in range(1, j+1):
            if start + k == data[j-k][i]:
                temp += 1
            elif start - k == data[j-k][i]:
                temp += 1
            else:
                break
        if temp > count:
            count = temp

print(count)
