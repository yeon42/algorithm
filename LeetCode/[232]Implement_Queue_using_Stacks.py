'''
문제 해석
- 2개의 스택을 사용해 FIFO를 구현하기
- 구현된 queue은 push, top, pop, empty와 같은 normal queue을 모두 사용 가능

MyQueue 클래스
- void push(int x): x를 큐의 back에 둠
- int pop(): 큐의 front에 있는 요소 제거하고 반환
- int peek(): 큐의 front에 있는 요소 반환
- boolean empty(): 큐가 비어있으면 true 반환, 아니면 false 반환

* 스택의 기본 연산인 'push to back', 'peek/pop from front', 'size', 'is empty' 만 사용 가능
'''

from collections import deque

class MyQueue(object):
    
    def __init__(self):
        self.queue = deque()


    def push(self, x): # 큐의 back에 push
        return self.queue.append(x)
        

    def pop(self): # 큐의 front 제거하고 반환
        return self.queue.popleft()


    def peek(self): # 큐의 fron 반환
        return self.queue[0]
        

    def empty(self): # 큐 비어있으면 true, 아니면 false 반환
        return len(self.queue)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()