from collections import defaultdict

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            num = nums[right]
            count[num] += 1
            
            # Shrink window when the count of the current number exceeds k
            while count[num] > k:
                count[nums[left]] -= 1
                left += 1
            
            # Update the maximum subarray length
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len