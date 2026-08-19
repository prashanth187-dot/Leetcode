from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
       
        rows = defaultdict(int)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] |= (1 << (seat - 2))
        
       
        ans = 2 * n
        
       
        left_mask = 0b00001111
        right_mask = 0b11110000
        mid_mask = 0b00111100
        
        for mask in rows.values():
            can_left = (mask & left_mask) == 0
            can_right = (mask & right_mask) == 0
            can_mid = (mask & mid_mask) == 0
            
            if can_left and can_right:
                continue  
            elif can_left or can_right or can_mid:
                ans -= 1  
            else:
                ans -= 2  
                
        return ans