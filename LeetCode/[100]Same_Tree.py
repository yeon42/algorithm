'''
문제 해석
: 두 개의 이진트리 p와 q가 주어졌을 때, 둘이 같은지 아닌지 판별하자.
- true, false 반환
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p or not q: # 비어 있으면
            return p == q # 둘이 같은지 판별
        
        # recursion
        if p.val == q.val: # 같으면 재귀적으로 자식들도 같은지 판별
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)   
