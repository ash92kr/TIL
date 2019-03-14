import sys
sys.stdin = open("두 개의 숫자열_input.txt")

T = int(input())

for tc in range(T):

    N, M = map(int, input().split())   # N = A리스트 원소 개수, M = B리스트 원소 개수

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_sum = 0
    idx = 0

    if N > M:   # N과 M의 개수에 따라 반복 횟수가 달라짐
        idx = N - M + 1
    else:
        idx = M - N + 1

    for i in range(idx):
        temp = 0
        if N > M:   # N이 M보다 크면 B리스트의 원소를 기준으로 A리스트의 시작점이 바뀜
            for j in range(M):
                temp += A[j+i] * B[j]
        else:   #  M이 N보다 크면 A리스트의 원소를 기준으로 B리스트의 시작점이 바뀜
            for j in range(N):
                temp += A[j] * B[j+i]
        if max_sum < temp:   # 크기가 작은 쪽의 리스트를 한 번 돌면 max값과 비교
            max_sum = temp

    print("#{} {}".format(tc+1, max_sum))


