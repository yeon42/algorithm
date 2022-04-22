'''
- 이진트리의 루트값과 targetSum이라는 정수값이 주어짐
- root-to-leaf 경로의 모든 값의 합이 targetSum과 같다면 true를 반환
'''

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum -= root.val
        
        ans = self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
        return ans