class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=1
        while len(nums):
            if k*i not in nums:
                return k*i
                break
            i+=1
            
        