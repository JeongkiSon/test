'''queue 자료구조
선입선출 먼저들어온게 먼저 나감 queue = 대기열, 차례대로
python 에서 deque 라이브러리로 구현가능, 리스트로도 되는데 시간복잡도가 높다'''

from collections import deque  #덱 라이브러리

#큐 구현을 위해 deque 라이브러리 사용

queue = deque()

queue.append(5)  #deque 라이브러리에서 append는 list의 append와 동일, 마찬가지로 상수시간
queue.append(2)  
queue.append(3)
queue.append(7)
queue.popleft() #가장 왼쪽 걸 꺼냄 , 마찬가지로 상수시간
queue.append(1)
queue.append(4)
queue.popleft()
#데이터가 오른쪽에서부터 들어와서 왼쪽으로 나가는 형식


print(queue) #먼저 들어온 순서
queue.reverse()  #역순으로
print(queue) #역순

'''리스트로 queue구현할 때 pop으로 특정 원소 꺼내면 꺼낸 후의 원소 index재조정 하는 과정에서 O(n)만큼
시간복잡도 걸림'''