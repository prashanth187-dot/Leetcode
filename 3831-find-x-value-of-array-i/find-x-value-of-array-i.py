class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        # dp[r] stores the number of subarrays ending at the previous index
        # whose product modulo k equals r.
        dp = [0] * k

        for num in nums:
            val = num % k
            new_dp = [0] * k
            
            # Start a new subarray with the current element
            new_dp[val] += 1
            
            # Extend existing subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * val) % k] += dp[r]
            
            # Add counts from subarrays ending at current index to final answer
            for r in range(k):
                ans[r] += new_dp[r]
                
            dp = new_dp

        return ans