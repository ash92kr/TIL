import sys
sys.stdin = open("간단한 압축 풀기_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    letter = []

    for i in range(N):
        letter += list(map(str, input().split()))

    temp = ""

    print("#{}".format(tc+1))
    for i in range(0, len(letter), 2):
        temp += (letter[i] * int(letter[i+1]))

    for i in range(len(temp)):
        if i % 10 == 0 and not i == 0:
            print()
        print("{}".format(temp[i]), end="")
    print()
