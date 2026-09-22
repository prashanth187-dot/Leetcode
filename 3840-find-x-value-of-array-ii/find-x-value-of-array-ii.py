class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_cnt = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 1, 0, self.n - 1)

    def _merge(self, node, left_node, right_node):
        l_prod, l_cnt = self.tree_prod[left_node], self.tree_cnt[left_node]
        r_prod, r_cnt = self.tree_prod[right_node], self.tree_cnt[right_node]

        self.tree_prod[node] = (l_prod * r_prod) % self.k

        cnt = list(l_cnt)
        for rem in range(self.k):
            if r_cnt[rem] > 0:
                new_rem = (l_prod * rem) % self.k
                cnt[new_rem] += r_cnt[rem]

        self.tree_cnt[node] = cnt

    def build(self, nums, node, start, end):
        if start == end:
            val = nums[start] % self.k
            self.tree_prod[node] = val
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][val] = 1
            return

        mid = (start + end) // 2
        self.build(nums, 2 * node, start, mid)
        self.build(nums, 2 * node + 1, mid + 1, end)
        self._merge(node, 2 * node, 2 * node + 1)

    def update(self, node, start, end, idx, val):
        if start == end:
            rem = val % self.k
            self.tree_prod[node] = rem
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][rem] = 1
            return

        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)

        self._merge(node, 2 * node, 2 * node + 1)

    def query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return self.tree_prod[node], self.tree_cnt[node]

        mid = (start + end) // 2
        if r <= mid:
            return self.query(2 * node, start, mid, l, r)
        if l > mid:
            return self.query(2 * node + 1, mid + 1, end, l, r)

        l_prod, l_cnt = self.query(2 * node, start, mid, l, r)
        r_prod, r_cnt = self.query(2 * node + 1, mid + 1, end, l, r)

        comb_prod = (l_prod * r_prod) % self.k
        comb_cnt = list(l_cnt)
        for rem in range(self.k):
            if r_cnt[rem] > 0:
                new_rem = (l_prod * rem) % self.k
                comb_cnt[new_rem] += r_cnt[rem]

        return comb_prod, comb_cnt


class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        st = SegmentTree(nums, k)
        res = []

        for idx, val, start, target_x in queries:
            st.update(1, 0, n - 1, idx, val)
            _, cnt = st.query(1, 0, n - 1, start, n - 1)
            res.append(cnt[target_x])

        return res