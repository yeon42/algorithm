'''
문제 해석
: 이진트리 root가 주어졌을 때, maximum depth를 리턴해라
- 루트 노드 ~ 리프 노드까지의 path 중 가장 긴 path의 노드 수

'''

# Recursion
class Solution(object):
    def maxDepth(self, root):
        # 빈 트리면 깊이 0
        if not root:
            return 0

        # 최상단 루트 노드 개수 +1 해주기
        ans = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        return ans