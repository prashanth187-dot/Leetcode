class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=n
        prod=1
        s1=0
        while n>0:
            last=n%10
            s1+=last
            prod*=last
            n=n//10
        s=s1+prod
        if a%s==0:
            return True
        else:
            return False

        