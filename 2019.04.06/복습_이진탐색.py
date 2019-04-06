
def binary_search(start, end, find):

    while start <= end:

        mid = (start + end) // 2

        if find == data[mid]:
            return mid + 1
        elif find > data[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


N = int(input())
data = list(map(int, input().split()))

T = int(input())
find = list(map(int, input().split()))

for i in range(T):
    binary_search(0, N-1, find[i])