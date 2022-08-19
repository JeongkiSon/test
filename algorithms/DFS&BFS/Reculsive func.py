'''재귀함수: 자기자신 다시 호출'''


'''

def reculsive_function():
    print('재귀함수를 호출')
    reculsive_function() 
    
    #무한히 반복
    
reculsive_function()   # maximum recursion depth exceeded while calling a Python object
#최대 재귀 깊이 초과 오류
함수가 재귀적으로 호출 = 컴퓨터 stack에 함수가 계쏙 쌓이는 형식, 언젠간 메모리 초과됨 = 재귀 깊이 제한
무한 호출 막기 위해 종료조건!! 포함
'''

def reculsive_function(i):
    #100번째 호출에서 종료
    if i == 100:
        return

    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다')
    reculsive_function(i + 1)

    print(i, '번째 재귀함수 종료')

#reculsive_function(1)


def factorial_iteration(n):
    result = 1
    
    for i in range(1, n + 1):
        result *= i
    
    return result

print(factorial_iteration(5)) #반복으로 구현

def factorial_reculsive(n):
    if n <= 1:
        return 1
    
    return n * factorial_reculsive(n - 1)  #나주엥 1 factorial 은 1 리턴합

print(factorial_reculsive(5)) #재귀로 구현
                                   
#유클리드 호제법, 최대공약수 계산 (재귀 예제)

'''
유클리드 호제법
자연수 A, B (A>B) 에서 A를 B로 나눈 나머지를 R
이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다
이 아이디어를 재귀로 구현 가능
GCD = Greatest Common Divisor 최대 공약수

GCD(192, 162)
    A       B
    192     162
    162     30
    30      12
    12      6

'''

def gcd(a, b):
    if a % b ==0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192, 162)) #a가 b보다 안 커도 됨
    
'''모든 재귀는 반복문으로 마들 수 있다
재귀가 반복문보다 유리할 수도 불리할 수도
컴퓨터가 함수 재귀로 호출 -> 메모리 내부의 스택 프레임에 쌓임
그래서 스택을 쓸 때 스택 라이브러리 대신에 재귀함수 이요하는 경우 많다'''    
    



