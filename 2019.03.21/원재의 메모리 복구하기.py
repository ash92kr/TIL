import sys
sys.stdin = open("원재의 메모리 복구하기_input.txt")

T = int(input())

for tc in range(T):

    data = list(map(int, input()))

    raw = [0] * len(data)

    count = 0
    flag = 1

    for i in range(len(data)):
        if raw[i] != data[i]:
            for j in range(i, len(data)):
                raw[j] = flag
            if flag:
                flag = 0
            else:
                flag = 1
            count += 1

    print("#{} {}".format(tc+1, count))

