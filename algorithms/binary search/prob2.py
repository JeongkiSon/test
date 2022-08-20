from bisect import bisect_left, bisect_right


# O(logN)으로 짜야 함

n, x = map(int, input().split())

arr = list(map(int, input().split()))



if x not in arr:
    print(-1)
else:
    a = bisect_left(arr, x)
    b = bisect_right(arr, x)
    print(b-a)
           



