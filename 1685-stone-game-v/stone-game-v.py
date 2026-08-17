class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0

        # Prefix sums for O(1) subarray sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]

        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            mid = 0
            for l in range(n - length + 1):
                r = l + length - 1
                
                if mid < l:
                    mid = l

                # Advance mid to find the split where left_sum <= right_sum
                total = pref[r + 1] - pref[l]
                while mid < r and (pref[mid + 1] - pref[l]) * 2 <= total:
                    mid += 1

                res = 0
                
                # Case 1: left_sum < right_sum for split points in range [l, mid - 1]
                if mid > l:
                    res = max(res, max_left[l][mid - 1])

                # Case 2: right_sum < left_sum for split points in range [mid + 1, r]
                if mid < r:
                    res = max(res, max_right[mid + 1][r])

                # Case 3: Check boundary mid where left_sum == right_sum
                left_sum = pref[mid] - pref[l]
                if mid > l and left_sum * 2 == total:
                    res = max(res, max_right[mid][r])

                dp[l][r] = res
                max_left[l][r] = max(max_left[l][r - 1], res + total)
                max_right[l][r] = max(max_right[l + 1][r], res + total)

        return dp[0][n - 1]