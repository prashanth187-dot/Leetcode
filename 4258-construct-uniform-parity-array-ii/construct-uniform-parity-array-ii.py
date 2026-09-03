class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Find all odd numbers
        odds = [x for x in nums1 if x % 2 != 0]
        
        
        if not odds:
            return True
            
        return min(nums1) == min(odds)