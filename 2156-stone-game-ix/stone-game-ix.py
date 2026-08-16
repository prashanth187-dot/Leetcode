class Solution(object):
    def stoneGameIX(self, stones):
        c0 = sum(1 for x in stones if x % 3 == 0)
        c1 = sum(1 for x in stones if x % 3 == 1)
        c2 = sum(1 for x in stones if x % 3 == 2)
        
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        return abs(c1 - c2) > 2