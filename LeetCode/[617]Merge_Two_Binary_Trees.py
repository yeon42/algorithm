'''
문제 해석
- 2개의 이진 트리 root1, root2가 주어짐
- 두 트리를 하나의 이진 트리로 합치기
- rule: 만약 두 노드가 overlap되면, 합쳐진 노드는 두 노드의 합이 됨

return: 합쳐진 트리
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' Recursion '''
class Solution(object):
    def mergeTrees(self, root1, root2):
        # 두 트리 중 하나가 빈 트리인 경우 그냥 나머지 트리 반환하고 끝!
        if not root1:
            return root2
        if not root2:
            return root1
        
        # 두 트리 모두 빈 트리가 아니라면
        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1


# if __name__ == "__main__":
#     root1 = [1]
#     root2 = [1, 2]
#     sol = Solution()
#     print(sol.mergeTrees(root1, root2))
 