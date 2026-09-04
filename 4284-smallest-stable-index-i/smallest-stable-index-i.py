class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        ind=n-1
        c=0
        for i in range(0,n):
            e1=max(nums[0:i+1])
            e2=min(nums[i:n])
            instable=e1-e2
            if instable<=k:
                ind=min(ind,i)
                c+=1
        if c==0:
            return -1
        return ind
                
        