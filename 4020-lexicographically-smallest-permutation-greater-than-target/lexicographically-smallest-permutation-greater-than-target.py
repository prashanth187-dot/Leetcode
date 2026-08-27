from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Try to match the longest prefix of target
        matched_prefix = []
        for i in range(n):
            c = target[i]
            if counts[c] > 0:
                matched_prefix.append(c)
                counts[c] -= 1
            else:
                break

        # If we matched all n characters, we cannot produce an equal string,
        # so backtrack 1 character to force a strictly greater character.
        if len(matched_prefix) == n:
            last = matched_prefix.pop()
            counts[last] += 1

        # Try to find a valid divergence point working backward from the prefix length
        for i in range(len(matched_prefix), -1, -1):
            if i < len(matched_prefix):
                # Backtrack: restore character at index i back to available pool
                counts[matched_prefix[i]] += 1
            
            target_char = target[i]
            # Look for the smallest available char strictly greater than target[i]
            for ch_code in range(ord(target_char) + 1, ord('z') + 1):
                ch = chr(ch_code)
                if counts[ch] > 0:
                    counts[ch] -= 1
                    prefix = matched_prefix[:i] + [ch]
                    
                    # Fill remaining positions with leftover characters in sorted order
                    suffix = []
                    for code in range(ord('a'), ord('z') + 1):
                        c_rest = chr(code)
                        suffix.append(c_rest * counts[c_rest])
                        
                    return "".join(prefix) + "".join(suffix)
        
        return ""