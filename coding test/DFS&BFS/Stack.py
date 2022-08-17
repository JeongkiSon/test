'''stack 자료구조
선입후출 먼저 들어온 것이 나중에 나가는 자료구조
python 에서 stack 자료구조를 이용하려면 list 자료형을 이용하면 됨
list에서 append와 pop이 stack의 push , pop임
append는 가장 오른쪽에 원소를 삽입하고, pop은 가장 오른쪽 걸 꺼냄
append 와 pop은 시간 복잡도가 O(1):상수 시간임 그냥 넣고 꺼내면 되니까
python 의 list자료형 == stack!!'''

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터, 가장 나중에 들어간거부터
print(stack) #최하단, 가장 먼저 들어간거 부터
