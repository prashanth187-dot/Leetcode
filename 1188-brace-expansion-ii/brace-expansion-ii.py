class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        groups = [[]]
        level = 0
        start = 0
        
        for i, char in enumerate(expression):
            if char == '{':
                if level == 0:
                    start = i + 1
                level += 1
            elif char == '}':
                level -= 1
                if level == 0:
                    # Expand inner nested brace recursively
                    sub_res = self.braceExpansionII(expression[start:i])
                    groups[-1].append(sub_res)
            elif level == 0:
                if char == ',':
                    groups.append([])
                else:
                    groups[-1].append([char])

        # Cross product (concatenation) within groups, then union across commas
        res = set()
        for group in groups:
            cur = {""}
            for word_list in group:
                cur = {a + b for a in cur for b in word_list}
            res.update(cur)

        return sorted(list(res))