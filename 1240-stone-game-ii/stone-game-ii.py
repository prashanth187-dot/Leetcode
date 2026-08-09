from functools import cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Calculate suffix sums to quickly get total remaining stones from index i
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @cache
        def dp(i: int, m: int) -> int:
            # If the current player can take all remaining piles, do so
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            # Try taking X piles (1 <= X <= 2 * m) and maximize total score
            max_stones = 0
            for x in range(1, 2 * m + 1):
                # Current player score = (Total remaining stones) - (Stones opponent gets)
                max_stones = max(max_stones, suffix_sum[i] - dp(i + x, max(m, x)))
                
            return max_stones
        
        return dp(0, 1)