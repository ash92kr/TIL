import sys
sys.stdin = open("최빈수 구하기_input.txt")


T = int(input())

for tc in range(T):

    N = int(input())

    array = [0] * 101

    score = list(map(int, input().split()))

    for i in range(len(score)):
        array[score[i]] += 1

    cnt = 0
    idx = 0

    for i in range(len(array)):
       if array[i] >= cnt:
           cnt = array[i]
           idx = i

    print("#{} {}".format(N, idx))
