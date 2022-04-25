'''
문제 해석
- 2개의 큐를 사용해 LIFO를 구현하기
- 구현된 stack은 push, top, pop, epty와 같은 normal stack을 모두 사용 가능

MyStack 클래스
- void push(int x): x를 스택의 top에 둠
- int pop(): 스택의 top에 있는 요소 제거하고 반환
- int top(): 스택의 top에 있는 요소 반환
- boolean empty(): 스택이 비어있으면 true 반환, 아니면 false 반환

* 큐의 기본 연산인 'push to back', 'peek/pop from front', 'size', 'is empty' 사용 가능
'''


from collections import deque

class MyStack(object):
    
    def __init__(self):
        self.queue = deque() # deque 생성
        
    def push(self, x): # top에 push
        self.queue.appendleft(x)

    def pop(self): # top 요소 제거하고 반환
        return self.queue.popleft() # top이므로 popleft

    def top(self): # top의 요소 반환 (제거 x)
        return self.queue[0]

    def empty(self): # 비어있으면 true, 아니면 false
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()