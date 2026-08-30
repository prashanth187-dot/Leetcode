class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # Find indices of minimum and maximum elements
        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))
        
        # Ensure first_idx <= second_idx
        first_idx = min(mini, maxi)
        second_idx = max(mini, maxi)
        
        # Scenario 1: Both removed from front
        option1 = second_idx + 1
        
        # Scenario 2: Both removed from back
        option2 = n - first_idx
        
        # Scenario 3: One from front, one from back
        option3 = (first_idx + 1) + (n - second_idx)
        
        return min(option1, option2, option3)