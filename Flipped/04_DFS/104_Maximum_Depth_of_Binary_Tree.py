class Solution(object):
    def maxDepth(self, root):
        
        if not root:
            return 0
        # print(root.left)
        # print(root.right)
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1