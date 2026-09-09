class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        p=1000
        while p<=n:
            ans+=n-p+1
            p*=1000
        return ans
        
        