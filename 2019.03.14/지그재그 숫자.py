import sys
sys.stdin = open("지그재그 숫자_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    zigzag = 0

    if N % 2 == 0:   # N이 짝수면 짝수+홀수 = -1이므로 -1 * (N//2)를 더함
        zigzag = (-1 * (N//2))
    else:
        zigzag = (-1 * (N//2)) + N  # 마지막 부분의 N만 더함

    print("#{} {}".format(tc+1, zigzag))
