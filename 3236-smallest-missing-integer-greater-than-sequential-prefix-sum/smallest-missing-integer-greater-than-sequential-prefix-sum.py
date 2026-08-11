class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Find the longest sequential prefix
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1
            
        # Step 2: Convert nums to a set for O(1) lookup speed
        num_set = set(nums)
        
        # Step 3: Find the smallest missing integer >= sum
        while s in num_set:
            s += 1
            
        return s