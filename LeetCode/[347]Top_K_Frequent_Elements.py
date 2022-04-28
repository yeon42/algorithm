'''
문제 해석
- 정수 배열 nums와 정수 k가 주어졌을 때, 가장 많이 등장하는 원소 k개를 반환해라.
'''

import collections

class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # col = collections.Counter(nums)
        # return col
        col = collections.Counter(nums)
        most_common = col.most_common(k)

        result = []
        for i in range(k):
            result.append(most_common[i][0])
        # result = [most_common[i][0] for i in range(k)]

        return result

        
        