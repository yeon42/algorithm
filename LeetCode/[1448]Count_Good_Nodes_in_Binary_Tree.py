'''
문제 해석
: 이진트리 root가 주어질 때,
root에서부터 노드 X까지의 경로에서 X보다 큰 노드 값이 없다면 good.
- 반환: good인 노드의 수
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countgoodNodes(self, root, val):
        if not root:
            return 0
        
        if root.val >= val: # max값보다 크면
            temp = 1
        else: # 1 < 3
            temp = 0
        
        val = max(val, root.val)
        temp += self.countgoodNodes(root.left, val)
        temp += self.countgoodNodes(root.right, val)

        return temp

    def goodNodes(self, root):
        return self.countgoodNodes(root, root.val)