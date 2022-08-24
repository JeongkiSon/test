#화폐 구성
'''
DP 문제 -> 점화식 생각!!
ai = i원 만드는데 필요한 최소량

k = 각 화폐 단위

각 k를 확인하며
ai-k를 만드는 방법이 존재하면 ai = min(ai, ai-k + 1)
ai-k 만드는 방법이 존재하지 않는 경우 ai = INF


'''


n , m = map(int, input().split()) #2 6원

list = []

for i in range(n):
    a = int(input())
    list.append(a)
    
dp= [10001] * (m + 1)
dp[0] = 0


for k in list:
    for j in range(k, m+1):
        dp[j] = min(dp[j], dp[j - k] + 1)
        
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])


