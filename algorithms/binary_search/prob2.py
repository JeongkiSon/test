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
           

'''
값이 [left_value , right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)
    return right_index - left_index
'''
