class Solution(object):

    def smallestIndex(self, nums):
        """
        :type nums: List[int]

        :rtype: int
        """
        for i in range(len(nums)):
            n = nums[i]
            s = 0

            if n == 0:
                s = 0
            else:
                while n > 0:
                    s += n % 10
                    n //= 10

            if s == i:
                return i

        return -1