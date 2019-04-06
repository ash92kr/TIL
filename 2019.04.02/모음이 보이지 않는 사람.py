import sys
sys.stdin = open("모음이 보이지 않는 사람_input.txt")

T = int(input())

for tc in range(T):

    vowel = ["a", "e", "i", "o", "u"]

    word = list(map(str, input()))

    print("#{}".format(tc+1), end=" ")
    for i in range(len(word)):
        if word[i] not in vowel:
            print(word[i], end="")
    print()