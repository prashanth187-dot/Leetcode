class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lmax=0
        rmax=0
        total=0
        l=0
        n=len(height)
        r=n-1
        while l<r:
            if height[l]<=height[r]:
                if height[l]<lmax:
                    total+=lmax-height[l]
                else:
                    lmax=height[l]
                l+=1
            else:
                if height[r]<rmax:
                    total+=rmax-height[r]
                else:
                    rmax=height[r]
                r-=1
        return total
        