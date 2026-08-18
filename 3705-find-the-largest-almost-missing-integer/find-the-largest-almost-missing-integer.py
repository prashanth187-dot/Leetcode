class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = {}
        n_len = len(nums)
        
        for n in set(nums):
            counts[n] = 0
            for i in range(n_len - k + 1):
                if n in nums[i : i + k]:
                    counts[n] += 1
                    
        valid_numbers = [num for num, count in counts.items() if count == 1]
        
        return max(valid_numbers) if valid_numbers else -1