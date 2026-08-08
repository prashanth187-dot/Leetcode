class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        prefix=[0]*n
        suffix=[0]*n
        prefix[0]=height[0]
        suffix[n-1]=height[n-1]
        for i in range(1,n-1):
            prefix[i]=max(prefix[i-1],height[i])
            suffix[n-i-1]=max(suffix[n-i],height[n-i-1])
        total=0
        for i in range(0,n-1):
            leftmax=prefix[i]
            rightmax=suffix[i]
            if height[i]<leftmax and height[i]<rightmax:
                total+=min(leftmax,rightmax)-height[i]
        return total

        