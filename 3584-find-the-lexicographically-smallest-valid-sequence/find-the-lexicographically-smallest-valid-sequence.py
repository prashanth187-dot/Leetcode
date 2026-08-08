class Solution(object):

    def validSequence(self, word1, word2):
        n, m = len(word1), len(word2)

      
        last = [-1] * (m + 1)
        last[m] = n

        ptr = n - 1
        for i in range(m - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[i]:
                ptr -= 1
            if ptr >= 0:
                last[i] = ptr
                ptr -= 1
            else:
                break

        res = []
        changed = False
        i = 0  

        for j in range(m):
            found = False
            while i < n:
                if word1[i] == word2[j]:
                    res.append(i)
                    i += 1
                    found = True
                    break
                elif not changed and last[j + 1] > i:
                    changed = True
                    res.append(i)
                    i += 1
                    found = True
                    break
                i += 1

            if not found:
                return []

        return res