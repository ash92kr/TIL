import sys
sys.stdin = open("백만장자 프로젝트_input.txt")

T = int(input())

for tc in range(T):

    N = int(input())

    price = list(map(int, input().split()))

    profit = 0

    while len(price) > 0:

        idx = price.index(max(price))   # .index 함수 사용하면 메모리 적게 차지한다

        temp = price[:idx+1]   # idx는 동적으로 계속 변화한다
        price = price[idx + 1:]

        for j in range(len(temp)-1):  # 역순이 메모리를 더 차지한다
            profit += (temp[-1] - temp[j])

    print("#{} {}".format(tc + 1, profit))


        # for i in range(len(price)):
        #     if price[i] == highest:
        #         temp = price[:i+1]
        #         price = price[i+1:]
        #         break
        #
        # for j in range(len(temp)-1, -1, -1):
        #     profit += (temp[-1] - temp[j])

    # print("#{} {}".format(tc + 1, profit))

        # for i in range(N):
        #     if price[i] == highest:
                # for j in range(i-1, -1, -1):
                #     profit += (max(price) - price[j])
                #     price.pop(j)
                # price.pop(0)
                # break

    # temp_price = [price[0]]
    #
    # for i in range(1, N):
    #     if temp_price[-1] > price[i]:
    #         for j in range(len(temp_price)-1):
    #             profit += (temp_price[-1]-temp_price[j])
    #         temp_price = [price[i]]
    #     else:
    #         temp_price.append(price[i])
    #
    # if len(temp_price) != 1:
    #     for k in range(len(temp_price)-1):
    #         profit += (temp_price[-1]-temp_price[k])

    # print("#{} {}".format(tc+1, profit))
