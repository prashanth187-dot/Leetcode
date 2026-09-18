class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find first and last occurrences of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        intervals = []
        
        # Step 2: Expand intervals for each character
        for ch in first:
            l = first[ch]
            r = last[ch]
            
            valid = True
            i = l
            while i <= r:
                # Expand right boundary if a character inside extends past 'r'
                r = max(r, last[s[i]])
                # If a character inside starts before 'l', this starting point is suboptimal/invalid
                if first[s[i]] < l:
                    valid = False
                    break
                i += 1
                
            if valid:
                intervals.append((r, l))  # Store as (end, start) for easy sorting
                
        # Step 3: Sort by end index (greedy interval scheduling)
        intervals.sort()
        
        ans = []
        last_end = -1
        
        for r, l in intervals:
            if l > last_end:
                ans.append(s[l:r+1])
                last_end = r
                
        return ans