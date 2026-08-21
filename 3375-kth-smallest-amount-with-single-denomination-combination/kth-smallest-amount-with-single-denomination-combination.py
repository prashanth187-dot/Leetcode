from fractions import gcd
from itertools import combinations

class Solution(object):
    def findKthSmallest(self, coins, k):
        def count(val):
            total = 0
            n = len(coins)
            for i in range(1, n + 1):
                for combo in combinations(coins, i):
                    lcm_val = combo[0]
                    for c in combo[1:]:
                        lcm_val = (lcm_val * c) // gcd(lcm_val, c)
                    
                    if i % 2 == 1:
                        total += val // lcm_val
                    else:
                        total -= val // lcm_val
            return total

        low = min(coins)
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans