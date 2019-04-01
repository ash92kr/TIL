import sys
sys.stdin = open("IM_A1_뽑기상자_input.txt")


# a = [2, 3, 3, 3]
#
# b = {}
#
# for i in range(len(a)):
#     if b.keys() not in a[i]:
#         b[a[i]] = 1
#     else:
#         b[a[i]] += 1
#
# print(b)

N = int(input())

kim = list(map(int, input().split()))
park = list(map(int, input().split()))

kim.sort()
park.sort()

kim_d = {}
park_d = {}

for i in range(N):
    if kim_d.get(kim[i], 0) == 0:
        kim_d[kim[i]] = 1
    else:
        kim_d[kim[i]] += 1

    if park_d.get(park[i], 0) == 0:
        park_d[park[i]] = 1
    else:
        park_d[park[i]] += 1

# print(kim_d)
# print(park_d)

count = 0

for i in range(1, 6):
    if i in park_d.keys() and i in kim_d.keys():
        count += abs(kim_d.get(i) - park_d.get(i))
    elif i not in park_d.keys() and i in kim_d.keys():
        count += kim_d.get(i)
    elif i not in kim_d.keys() and i in park_d.keys():
        count += park_d.get(i)


# print(count)

if count % 4 == 0:  # count가 4배수라면 교환을 통한 완전일치 가능
    print(count//4)   # 1번 교환에 2개 구슬을 바꿀 수 있다
                      # (차이나는 구슬의 개수는 처음부터 2배씩 곱해지기 때문에 4로 나눔)
else:  # count가 홀수면 교환해서 완전일치 불가
    print(-1)



# print(kim_d, park_d)
#

#
# count = 0
# temp = 0
#
# i = 0
# j = 1

# while i < N:
#
#     kim[i], park[i] = park[i], kim[i]
#
#     kim_d = {}
#     park_d = {}
#
#     for j in range(N):
#         if kim_d.get(kim[j], 0) == 0:
#             kim_d[kim[j]] = 1
#         else:
#             kim_d[kim[j]] += 1
#
#         if park_d.get(park[j], 0) == 0:
#             park_d[park[j]] = 1
#         else:
#             park_d[park[j]] += 1
#
#     if kim_d == park_d:
#         count = 1
#         break
#     else:
#         kim[i], park[i] = park[i], kim[i]
#         i += 1

# if count == 0:
#     print(-1)
# else:
#     print(count)