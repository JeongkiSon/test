
'''
n, m = map(int, input().split())

arr = list(map(int, input().split()))
# 19 15 10 17

for i in range(max(arr), 0 , -1): #19
    sub = []
    for j in range(len(arr)):
        a = 0
        if arr[j] - i <= 0:
            a = 0
        else: a = arr[j] - i
        #sub.append(a)
    
    if sum(sub) >= m:
        print(sub)
        print(i)
        break
    

n, m = map(int, input().split())

arr = list(map(int, input().split()))
'''

'''
#절단기의 높이는 0부터 10억까지의 정수 중 하나이므로
#이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 한다

시작점 0 끝점 19 중간점 9일 때 OK
시작점 10 끝점 19 중간점 14일 때 잘린 떡 길이 6보다 크므로 OK
시작점 15 끝점 19 중간점 17  잘린 떡 2라서 안됨 X
시작점 15 끝점 16 중간점 15 잘린 떡 6이라서 딱 6

중간점은 시간이 지날수록 최적화된 값

떡 길이가 조건보다 크거나 같을 때만 중간점 값을 기록

'''

n , m = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)


result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    
    for x in arr:
        if x - mid >= 0:
            total += x - mid
    
        
    if total >= m:
        result = mid
        start = mid + 1  
    else:
        end = mid - 1
    

print(result)







