'''
문제 해석
: 이진트리의 root가 주어졌을 때, inorder traversal(중위 순회)을 통해 노드 값들을 리스트로 반환해라
(왼쪽 자식 -> 부모 -> 오른쪽 자식)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)