class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        ans = ""
        
        
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        
        if len(ones) < k:
            return ""
        
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            
            if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                ans = sub
                
        return ans