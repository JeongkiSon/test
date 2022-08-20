'''
순차 탐색: 리스트 안 특정 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인
이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
이진 탐색은 시작점 끝점 중간점을 이용해서 탐색 범위를 설정함

시간 복잡도 탐색 범위가 절반 되므로 연산 횟수는 log2N에 비례

탐색 범위를 절반씩 줄이기에 시간 복잡도는 O(log N)

'''

from xml.dom import INDEX_SIZE_ERR


arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def func(arr, start, end, target):
    
    mid = int((start + end) / 2 ) 
    

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
    else: start = mid + 1

    return func(arr, start, end, target)

print(func(arr, 0, 9, 18) )
    
'''
while start<= end:
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target
        end = mid - 1
    else: start = mid + 1   
    
    '''
    
'''
파이썬 이진 탐색 라이브러리
bisect_left(a, x) :정렬 된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_left(a, x) :정렬 된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환



'''

'''
Parametric Search 파라메트릭 서치

최적화 문제를 결정문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
e.g., 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

일반적인 코테에서 Parametric Search 는 이진 탐색으로 해결가능


'''


