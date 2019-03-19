import sys
sys.stdin = open("중간 평균값 구하기_input.txt")

T = int(input())

for tc in range(T):

    data = list(map(int, input().split()))

    for i in range(len(data)-1):  # 버블 정렬
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    min_max = 0   # 최소, 최대값을 제외한 원소들의 합을 넣을 공간
    idx = 0

    for i in range(1, len(data)-1):
        min_max += data[i]
        idx += 1

    print("#{} {}".format(tc+1, round(min_max/idx)))

