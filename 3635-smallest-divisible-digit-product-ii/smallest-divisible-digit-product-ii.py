class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # Step 1: Decompose t into prime factors 2, 3, 5, 7
        count = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while t % p == 0:
                count[p] += 1
                t //= p
        
        if t > 1:
            return "-1"

        def get_min_digits_for_factors(c2, c3, c5, c7):
            """
            Finds the optimal digit combination (counts of 2..9) to satisfy 
            c2, c3, c5, c7 while minimizing the total number of digits used.
            """
            best_digits = None
            min_length = float('inf')

            # c5 and c7 can only be satisfied by 5 and 7
            # We try all valid combinations of 8s, 9s, 6s, 4s, 3s, 2s
            for c8 in range(c2 // 3, -1, -1):
                rem2_8 = c2 - c8 * 3
                for c9 in range(c3 // 2, -1, -1):
                    rem3_9 = c3 - c9 * 2
                    
                    for c6 in range(min(rem2_8, rem3_9), -1, -1):
                        rem2_6 = rem2_8 - c6
                        rem3_6 = rem3_9 - c6
                        
                        for c4 in range(rem2_6 // 2, -1, -1):
                            rem2_4 = rem2_6 - c4 * 2
                            
                            c2_final = rem2_4
                            c3_final = rem3_6
                            
                            total_digits = c2_final + c3_final + c4 + c5 + c6 + c7 + c8 + c9
                            if total_digits < min_length:
                                min_length = total_digits
                                best_digits = (c2_final, c3_final, c4, c5, c6, c7, c8, c9)

            return best_digits if best_digits else (c2, c3, 0, c5, 0, c7, 0, 0)

        def required_digits_count(c2, c3, c5, c7):
            return sum(get_min_digits_for_factors(c2, c3, c5, c7))

        def get_suffix(length, c2, c3, c5, c7):
            digits = get_min_digits_for_factors(c2, c3, c5, c7)
            total_needed = sum(digits)
            ones = length - total_needed
            if ones < 0:
                return None
            
            res = ['1'] * ones
            for d, cnt in zip(range(2, 10), digits):
                res.extend([str(d)] * cnt)
            return "".join(res)

        digit_factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        n = len(num)
        pref_2, pref_3, pref_5, pref_7 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        first_zero = n
        
        for i in range(n):
            d = int(num[i])
            if d == 0:
                first_zero = i
                break
            d2, d3, d5, d7 = digit_factors[d]
            pref_2[i+1] = pref_2[i] + d2
            pref_3[i+1] = pref_3[i] + d3
            pref_5[i+1] = pref_5[i] + d5
            pref_7[i+1] = pref_7[i] + d7

        # Case 1: Match prefix up to position i, then try d_next > num[i]
        for i in range(min(n, first_zero), -1, -1):
            if i == n:
                if (pref_2[n] >= count[2] and pref_3[n] >= count[3] and 
                    pref_5[n] >= count[5] and pref_7[n] >= count[7]):
                    return num
                continue

            start_d = int(num[i]) + 1
            for d_next in range(start_d, 10):
                d2, d3, d5, d7 = digit_factors[d_next]
                req2 = max(0, count[2] - pref_2[i] - d2)
                req3 = max(0, count[3] - pref_3[i] - d3)
                req5 = max(0, count[5] - pref_5[i] - d5)
                req7 = max(0, count[7] - pref_7[i] - d7)
                
                rem_len = n - 1 - i
                if required_digits_count(req2, req3, req5, req7) <= rem_len:
                    suf = get_suffix(rem_len, req2, req3, req5, req7)
                    if suf is not None:
                        return num[:i] + str(d_next) + suf

        # Case 2: Length n + 1 (or minimum length needed to satisfy factor counts)
        min_len = max(n + 1, required_digits_count(count[2], count[3], count[5], count[7]))
        return get_suffix(min_len, count[2], count[3], count[5], count[7])