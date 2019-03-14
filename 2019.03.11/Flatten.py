import sys
sys.stdin = open("Flatten_input.txt")

def order(box):

    for i in range(len(box)-1):
        for j in range(i+1, len(box)):
            if box[i] > box[j]:  # 방향 위치 주의할 것(> 는 오름차순, < 는 내림차순)
                box[i], box[j] = box[j], box[i]   # 그에 따라 [0]과 [-1]이 완전히 달라짐


for tc in range(10):

    dump = int(input())

    box = list(map(int, input().split()))

    for i in range(dump):
        order(box)  # 속도가 느리긴 하다
        box[-1] -= 1
        box[0] += 1

    # min_box = 999
    # max_box = 0

    # for i in range(len(box)):
    #     if box[i] > max_box:
    #         max_box = box[i]
    #     if box[i] < min_box:
    #         min_box = box[i]

    # print("#{} {}".format(tc+1, max_box-min_box))
    print("#{} {}".format(tc+1, box[-2]-box[1]))   # 이미 실행한 이후이므로 안쪽으로 한칸 들어가야 한다


