import sys
sys.stdin = open("C9_기업투자_input.txt")

def DFS(n, r, total, money):  # nCr -> total: 임시 금액 변수, money: 깊이 변수

    global N, result

    if N == money:    # 가지의 끝까지 온 경우(기업에 투자한 모든 금액이 최대 금액인 경우)
        result = max(result, total)   # result와 total(임시 변수) 중 최대 금액 보관
        return

    if n == r:   # 가지의 끝까지 온 경우(해당 금액대의 모든 기업을 들른 경우)
        return

    for i in range(N+1):   # 돈의 액수만큼 선택
        DFS(n, r+1, total+info[r][i], money+i)   # 기업 개수 그대로, 다음 기업으로 넘어감, 임시금액에 해당 칸의 투자 이익 추가, 투자 금액에 i 추가

    return


N, M = map(int, input().split())

temp = [list(map(int, input().split())) for _ in range(N)]

info = [[0 for _ in range(len(temp)+1)] for _ in range(len(temp[0])-1)]

for i in range(len(temp)):
    for j in range(1, len(temp[0])):
        info[j-1][i+1] = temp[i][j]

# for i in range(len(info)):
#     print(i, info[i])

result = 0

DFS(M, 0, 0, 0)   # M = 기업 개수

print(result)