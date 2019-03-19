import sys
sys.stdin = open("시각 덧셈_input.txt")

T = int(input())

for tc in range(T):

    H1, M1, H2, M2 = map(int, input().split())

    T1 = H1 + H2
    T2 = M1 + M2

    if T2 >= 60:  # 분이 60분 이상이면 감소(%를 써서 나눌 수 있다)
        T2 -= 60
        T1 += 1

    if T1 >= 13:  # 시간이 13시간 이상이면 감소(%를 써서 구현할 수 있다)
        T1 -= 12

    print("#{} {} {}".format(tc+1, T1, T2))