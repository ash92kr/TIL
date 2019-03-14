import sys
sys.stdin = open("View_input.txt")

def max_temp(temp):

    for i in range(len(temp)-1):
        for j in range(i+1, len(temp)):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[j], temp[i]


for tc in range(10):

    N = int(input())

    building = list(map(int, input().split()))

    view = 0

    for i in range(2, len(building)-2):
        temp = []   # 앞뒤 2개 건물의 높이를 담기 위한 배열
        if building[i] > building[i-2] and building[i] > building[i-1] and building[i] > building[i+1] and building[i] > building[i+2]:
            temp.append(building[i-2])  # i의 높이가 앞뒤 2개 건물의 높이보다 가장 높으면
            temp.append(building[i-1])  # 남은 4개 건물을 리스트에 담는다
            temp.append(building[i+1])
            temp.append(building[i+2])
            max_temp(temp)  # 그리고 정렬을 통해 가장 큰 값을 구한다
            # if building[i] - temp[-1] > 0:
            view += building[i] - temp[-1]

    print("#{} {}".format(tc+1, view))

