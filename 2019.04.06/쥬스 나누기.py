import sys
sys.stdin = open("쥬스 나누기_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    print("#{}".format(tc+1), end=" ")
    for i in range(N):
        print("1/{}".format(N), end=" ")
    print()