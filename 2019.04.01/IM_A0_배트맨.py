import sys
sys.stdin = open("IM_A0_배트맨_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    height = list(map(int, input().split()))

    count = 0

    i = 0

    while i < N-1:

        if height[i] <= height[i+1]: # 빌딩 높이가 나랑 같거나 높으면 +1
            count += 1
        else:  # 낮을 경우
            temp = []
            temp.append(height[i])   # 현재 빌딩 높이를 우선 넣는다

            while i < N-1:

                if temp[-1] > height[i+1]:   # 빌딩이 낮으면 계속 통과하고
                    temp.append(height[i])
                    i += 1
                else:   # 이전 빌딩 높이가 현재 빌딩의 높이와 같거나 작으면
                    count += 1
                    break

        i += 1

    print(count)