import sys
sys.stdin = open("September9_input.txt")

T = int(input())

for tc in range(T):

    N = input()

    flag = 0

    for i in N:
        if i == "9":
            flag = 1

    if flag:
        print("#{} Yes".format(tc+1))
    else:
        print("#{} No".format(tc+1))

