class SegmentTree(object):
    def __init__(self, arr: list[int]):
        self._tree = [0] * (4 * len(arr))
        self._size = len(arr)
        self._build(arr, 0, 0, len(arr) - 1)

    def _build(self, arr: list[int], node: int, left: int, right: int) -> None:
        if left == right:
            self._tree[node] = arr[left]
        else:
            mid = (left + right) // 2
            self._build(arr, 2 * node + 1, left, mid)  # 左子树
            self._build(arr, 2 * node + 2, mid + 1, right)  # 右子树
            self._tree[node] = self._tree[2 * node + 1] + self._tree[2 * node + 2]

    def query(self, node: int, left: int, right: int, ql: int, qr: int) -> int:
        if left > qr or right < ql:
            return 0
        if ql <= left and right <= qr:
            return self._tree[node]
        else:
            mid = (left + right) // 2
            return self.query(2 * node + 1, left, mid, ql, qr) + self.query(2 * node + 2, mid + 1, right, ql, qr)

    def update(self, node: int, left: int, right: int, idx: int, val: int) -> None:
        # idx: 表示的是数组里面的 index
        if left == right:
            self._tree[node] = val
        else:
            mid = (left + right) // 2
            if idx <= mid:
                self.update(2 * node + 1, left, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, right, idx, val)
            self._tree[node] = self._tree[2 * node + 1] + self._tree[2 * node + 2]


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print(st._tree)
    print(st.query(0, 0, len(arr) - 1, 1, 4))  # 查询区间 [1, 4] 的和
    st.update(0, 0, len(arr) - 1, 2, 10)  # 更新索引 2 的值为 10
    print(st.query(0, 0, len(arr) - 1, 1, 4))  # 再次查询区间 [1, 4] 的和
