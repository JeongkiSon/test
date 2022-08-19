n, k = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

a.sort()
b.sort()
# cf b.sort(reverse = True) 하면 내림차순 정렬 수행
cnt = 0
while(cnt < k and a[cnt] < b[n-1-cnt]):
    a[cnt] , b[n-1-cnt] = b[n-1-cnt], a[cnt]
    cnt += 1

print(sum(a))















