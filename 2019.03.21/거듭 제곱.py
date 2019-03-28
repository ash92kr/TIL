import sys
sys.stdin = open("거듭 제곱_input.txt")

# def multiple(N):
#
#     return N

def multiple(M):

    if M == 1:
        return N
    else:
        return N * multiple(M-1)



for tc in range(10):

    T = int(input())

    N, M = map(int, input().split())

    print("#{} {}".format(T, multiple(M)))