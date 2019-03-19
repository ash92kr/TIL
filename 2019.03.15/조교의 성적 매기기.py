import sys
sys.stdin = open("조교의 성적 매기기_input.txt")

T = int(input())

for tc in range(T):

    N, K = map(int, input().split())

    data = []  # 학생 성적 받기

    for i in range(N):
        data.append(list(map(int, input().split())))

    # print(data)

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    jumsu = []   # 학생 성적 계산하는 배열

    for i in range(N):
        jumsu.append(round((data[i][0] * 0.35) + (data[i][1] * 0.45) + (data[i][2] * 0.2), 2))

    # print(jumsu)

    jumsu_k = jumsu[K-1]  # 인덱스이므로 K-1번째의 점수를 저장

    for i in range(0, N-1):   # 버블 정렬
        for j in range(i+1, N):
            if jumsu[i] < jumsu[j]:
                jumsu[i], jumsu[j] = jumsu[j], jumsu[i]

    # print(jumsu_k)
    # print(jumsu)

    for k in range(N):   # 저장된 점수와 일치하는 점수가 있다면
        if jumsu[k] == jumsu_k:
            if N == 10:  # 학생이 10명이면 그 인덱스에 해당하는 성적 출력
                print("#{} {}".format(tc+1, grade[k]))
            else:   # 학생이 100명이면 100으로 나눈 다음 10을 곱해 정수화된 인덱스의 성적 출력
                print("#{} {}".format(tc+1, grade[int((k/N)*10)]))

