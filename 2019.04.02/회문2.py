import sys
sys.stdin = open("회문2_input.txt")

for tc in range(10):

    N = int(input())

    data = [list(map(str, input())) for _ in range(100)]

    # print(data)

    length = 0

    for i in range(100):
        for j in range(100):
            for k in range(100-j-1, 0, -1):   # k는 회문을 확인할 문자열의 개수(100글자부터 1글자까지 확인)
                flag = 1
                for l in range((k+1)//2):   # l은 회문을 확인할 문자열 개수를 2로 나누어 양쪽 끝부터 안쪽으로 같은지 비교
                    if data[i][j+l] != data[i][j+k-l]:  # 왼쪽 시작점 j, 오른쪽 시작점 j+k
                        flag = 0  # 한 번이라도 틀리면 종료
                        break
                if flag == 1 and (k+1) > length:  # 회문이 맞고 현재 저장한 길이보다 긴 경우 k+1을 저장
                    length = (k+1)

    for i in range(100):
        for j in range(100):
            for k in range(100-j-1, 0, -1):
                flag = 1
                for l in range((k+1)//2):
                    if data[j+l][i] != data[j+k-l][i]:
                        flag = 0
                        break
                if flag == 1 and (k+1) > length:
                    length = (k+1)

    print("#{} {}".format(tc+1, length))


