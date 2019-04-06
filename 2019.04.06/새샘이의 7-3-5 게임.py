import sys
sys.stdin = open("새샘이의 7-3-5 게임_input.txt")

def DFS(depth, count):

    global sum_list

    if depth >= 3:
        if count == 3:
            temp = 0
            for i in range(3):
                temp += record[i]

            if temp not in sum_list:
                sum_list.append(temp)
        return

    for i in range(7):
        if check[i]:
            continue
        record[depth] = arr[i]
        check[i] = 1
        DFS(depth+1, count+1)
        check[i] = 0


T = int(input())

for tc in range(T):

    arr = list(map(int, input().split()))

    record = [0] * 3
    check = [0] * 7

    sum_list = []

    DFS(0, 0)

    sum_list.sort()

    print("#{} {}".format(tc+1, sum_list[-5]))