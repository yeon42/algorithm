# 5-1. 스택 예제

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) # 최상단 원소부터 출력

'''
파이썬에서 스택 이용시 별도의 라이브러리 사용할 필요 ㅇ벗고,
기본 리스트에서 append()와 pop() 메서드를 사용하면 된다.
'''