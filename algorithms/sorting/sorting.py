'''
정렬(sorting) 데이터를 특정한 기준에 따라 순서대로 나열

###########
선택 정렬
처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에
있는 데이터와 바꾸는 것을 반복
이중 반복문으로 구현 가능

시간 복잡도: n번 만큼 가장 작은 수를 찾아 탐색-> 맨앞으로 보냄
n + n-1 + n-2 ... + 2
==> (n^2 + n -2) / 2 이고 big-O notation 에 따라 O(N^2)

############
삽입 정렬
처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
선택 정렬보다 구현 난이도가 높지만, 속도가 빠르다

맨 앞 7은 정렬되어 있다 판단하고, 두번째인 5가
어디로 갈지 판단, 7의 왼쪽 or 오른쪽

시간 복잡도: O(N^2)임 선택정렬과 마찬가지로 반복문이 두 번 중첨
삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작

최선의 경우 O(N)의 시간 복잡도: 다 정렬되어 있는 경우

#######
퀵 정렬 quick sort
이름에서부터 빠른 정렬
기준 데이터(pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
병합정렬과 더불어 대부분 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(pivot)으로 설정

왼쪽 부터는 5보다 큰 거 고름 오른쪽 부터는 5보다 작은 데이터를 고름
그리고 위치 바꿈
위치가 엇갈리면 피봇과 작은 데이터의 위치를 서로 변경
피봇을 기준으로 데이터의 묶음을 나누는 작업을 분할(divide) partition

5기준 왼쪽배열에서 퀵정렬 따로
5기준 오른쪽배열에서 퀵정렬 따로 각각 해줌

빠른 이유
이상적인 경우 분할이 절반 씩 일어나면 전체 연산 횟수는 O(NlonN)이 될 수 있다
데이터 개수 N 이고 나누는 횟수는 logN 이니까 전체 연산 횟수는 NlogN

퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도

최악의 경우 O(N^2) 분할이 절반으로 안되고 편향되는 경우

첫번째 원소는 피봇 ,이미 정렬된 배열에 대해 퀵정렬을 하면  O(N^2)


#####
계수 정렬
특정한 조건에서만 쓸 수 있지만 매우 빠름
    계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용가능
 
데이터의 개수가 N, 데이터(양수)중 최대값이 K일 때 최악의 경우에도 수행시간
O(N + K)를 guarantee함

step1 가장 작은 데이터부터 큰 데이터까지의 범위가 모두 담길 수 있는 리스트 만들기 
step2 데이터를 확인하며 데이터 값과 동일한 인덱스의 데이터를 1씩 증가 데이터가 개수(count)임


'''

from operator import le
from winreg import QueryReflectionKey


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)): 
    min_index = i #가장 작은 원소의 인덱스 init = 0, 처음에는 제일 앞에꺼
    for j in range(i+1, len(arr)): #1~ end
        if arr[min_index] > arr[j]:
            min_index = j  #최소값 찾기
    arr[i], arr[min_index] = arr[min_index], arr[i] #swap

print(arr)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)): #2번째 원소부터 시행
    for j in range(i, 0, -1): #인덱스 i부터 1까지 1씩 감소하며 반복
        #pick하는 j기준 앞쪽은 다 정렬되어 있음
        
        if arr[j] < arr[j - 1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else:
            break

print(arr)



arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:
        return arr
    
    pivot = start
    pivot_value = arr[start]

    left = start + 1
    right = end
    
    while (left <= right):
        while (left <= end and arr[left] <= arr[pivot]): 
            #left값이 pivot보다 작다면 큰 거 나올 때까지 한 칸 이동
            left += 1
        
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        
        if left > right: #엇갈림 -> arr[rifht] 가 작은 값임
            arr[right], arr[pivot] = arr[pivot], arr[right]
            
        else:
            arr[left], arr[right] = arr[right], arr[left] #swap
    
    
    idx = arr.index(pivot_value)
    quick_sort(arr, start, idx - 1)
    quick_sort(arr, idx + 1, end)         

quick_sort(arr, 0, len(arr)-1)
print(arr)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 2, 4, 8, 0, 5, 2]

count = [0]* (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')


