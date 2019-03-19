import sys
sys.stdin = open("간단한 369게임_input.txt")

for tc in range(2):

    N = int(input())

    for i in range(1, N+1):
        count = 0
        for j in str(i):
            if j in ["3", "6", "9"]:
                print("-", end="")
                count += 1
        if count == 0:
            print(i, end=" ")
        else:
            print(end=" ")
    print()
