import sys
sys.stdin = open("C4_주사위 던지기1_input.txt")


def combination(depth, count):

    if depth >= N:
        return

    record[count] =
    combination(depth+1, count+1)

    record[count] = 0
    combination(depth+1, count)


def permutation(depth, count):

    if depth >= N:
        return

    for i in range(6):
        if check:
            continue
        record[i] = dice[count]
        check[i] = 1
        permutation(depth+1, count+1)
        check[i] = 0


dice = [1, 2, 3, 4, 5, 6]
N, M = map(int, input().split())

record = [0] * 6
check = [0] * 6

if M == 3:
    permutation(0, 0)
else:
    combination(0, 0)