class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num=set(nums)
        n=len(nums)//2
        if len(num)>n:
            return False
        nums.sort()
        left=0
        right=1
        s=False
        while right<len(nums):
            if nums[left]==nums[right]:
                s=True
                left=right+1
                right=right+2
            else:
                return False
        return s


        