import sys
sys.stdin = open("패턴마디의 길이_input.txt")

T = int(input())

for tc in range(T):

    word = list(map(str, input()))

    j = 0

    for i in range(1, 30):
        if word[i] == word[j]:
            j += 1
        else:
            j = 0   # 한 글자 혹은 그 이상이 같아도 패턴을 찾을 수 있다

    print("#{} {}".format(tc+1, 30-j))
