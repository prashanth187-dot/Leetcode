from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        # Pair elements with original indices and sort by value
        sorted_nums = sorted((val, i) for i, val in enumerate(nums))
        
        groups = []
        num_to_group = {}
        
        for val, orig_idx in sorted_nums:
            # If start of a new group (difference > limit), create a new queue
            if not groups or val - groups[-1][-1] > limit:
                groups.append(deque())
            
            groups[-1].append(val)
            num_to_group[val] = len(groups) - 1
            
        res = [0] * len(nums)
        for i, val in enumerate(nums):
            group_idx = num_to_group[val]
            # Take the smallest available value from the corresponding group
            res[i] = groups[group_idx].popleft()
            
        return res