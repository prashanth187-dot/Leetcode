from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        items = sorted([(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)])
        starts = [item[0] for item in items]

        @lru_cache(None)
        def dp(i: int, count: int):
            if i >= n or count == 0:
                return (0, ())

            
            res_val, res_indices = dp(i + 1, count)

           
            l, r, w, idx = items[i]
            next_i = bisect_right(starts, r)
            next_val, next_indices = dp(next_i, count - 1)
            
            take_val = w + next_val
            take_indices = tuple(sorted((idx,) + next_indices))

            
            if take_val > res_val:
                res_val, res_indices = take_val, take_indices
            elif take_val == res_val:
                if res_indices == () or take_indices < res_indices:
                    res_indices = take_indices

            return res_val, res_indices

        return list(dp(0, 4)[1])