class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        
        # Step 1: Precompute Suffix Minimums
        suffMin = [0] * n
        suffMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i + 1])
        
        # Step 2 & 3: Maintain running prefix max and check stability
        runningMax = float('-inf')
        for i in range(n):
            runningMax = max(runningMax, nums[i])
            
            # Instability score check in O(1)
            if runningMax - suffMin[i] <= k:
                return i
                
        return -1