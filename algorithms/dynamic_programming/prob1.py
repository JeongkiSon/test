#개미 전사

'''
창고 1까지만 알 때의 최대값은 1
창고 2까지만 알 때의 최대값은 3 -> 1번 선택 안하고 3선택
창고 3까지만 알 때의 최대값은 3 -> a1에 창고 3 더한값 < 창고2만 고른값
창고 4까지만 알 때의 최대값은 8 -> a2 + 창고4 = 8 > a3
bottom-up??
'''


n = int(input())

arr = list(map(int, input().split()))

dp = [0] * n


for i in range(n):
    if i == 0:
        dp[0] = arr[0]
    elif i == 1:
        dp[1] = max(dp[0], arr[1])
    else: #i>=2
        if arr[i] + dp[i-2] > dp[i-1]:
            dp[i] = arr[i] + dp[i-2]
        else: dp[i] = dp[i-1]

    if i == (n-1):
        print(dp[i])
        
        
'''
특정 단계까지의 최적의 해는 i-1과 i-2를 이용할 수 있다  #새끼문제꺼 이용가능

ai =  max(ai-1, ai-2 + ki)

'''


