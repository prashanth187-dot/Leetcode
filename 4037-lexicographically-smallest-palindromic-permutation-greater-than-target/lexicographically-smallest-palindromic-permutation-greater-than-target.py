from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        counts = Counter(s)
        
        # Validate if a palindromic permutation is possible
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Build frequency map for the first half
        half_counts = {ch: cnt // 2 for ch, cnt in counts.items()}
        
        def can_build_palindrome(first_half: str) -> str:
            """Constructs the full palindrome given the first half."""
            second_half = first_half[::-1]
            return first_half + mid_char + second_half

        # Helper to construct lexicographically smallest suffix for the first half
        def complete_half(current_prefix: str, rem_counts: dict) -> str:
            suffix = []
            for ch in sorted(rem_counts.keys()):
                suffix.append(ch * rem_counts[ch])
            return current_prefix + "".join(suffix)

        # Iterate through prefix lengths from longest to shortest match
        for i in range(m, -1, -1):
            prefix = target[:i]
            
            # Check if prefix target[:i] is buildable
            req_counts = Counter(prefix)
            if any(req_counts[ch] > half_counts.get(ch, 0) for ch in req_counts):
                continue
            
            # Remaining characters available after using `prefix`
            rem_counts = {ch: half_counts[ch] - req_counts.get(ch, 0) for ch in half_counts}
            
            # Case 1: Try placing a character c > target[i] at position i
            if i < m:
                target_char = target[i]
                for ch in sorted(rem_counts.keys()):
                    if ch > target_char and rem_counts[ch] > 0:
                        rem_counts[ch] -= 1
                        candidate_half = complete_half(prefix + ch, rem_counts)
                        candidate_pal = can_build_palindrome(candidate_half)
                        if candidate_pal > target:
                            return candidate_pal
                        rem_counts[ch] += 1
            
            # Case 2: Exact prefix match up to m
            elif i == m:
                candidate_half = prefix
                candidate_pal = can_build_palindrome(candidate_half)
                if candidate_pal > target:
                    return candidate_pal

        return ""