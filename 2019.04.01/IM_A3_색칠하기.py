import sys
sys.stdin = open("IM_A3_색칠하기_input.txt")


row, col, N = map(int, input().split())

pan = [[0 for _ in range(col)] for _ in range(row)]

for k in range(N):
    rec = list(map(int, input().split()))

    for i in range(rec[2]-rec[0]+1):   # col
        for j in range(rec[3]-rec[1]+1):   # row
            if pan[rec[0]+i][rec[1]+j] > rec[4]:
                break
            else:
                pan[rec[0]+i][rec[1]+j] = rec[4]

max_hab = 0
count = 0

for i in range(col):   # 그냥 rec[4]의 max값을 저장해도 됨
    for j in range(row):
        if pan[i][j] > max_hab:
            max_hab = pan[i][j]

for i in range(col):
    for j in range(row):
        if pan[i][j] == max_hab:
            count += 1

print(count)