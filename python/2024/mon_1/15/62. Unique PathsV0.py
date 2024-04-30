"""
这个方法和官方的动态规划思想一样，只是这里使用了递归实现(但是超时)
超时的问题在于不能递归增加了内存等的申请管理以及每次都重新计算值
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        des_total = 0
        # 用来保存已经存了的数据，有则get，没有则 add
        k_v = {}

        # 需要保证 a <= b a > 0 b > 0
        def get_count(a: int, b: int):
            nonlocal des_total, k_v
            if a > b:
                t = a
                a = b
                b = t
            if a == 1:
                des_total += 1
                return
            elif a == 2:
                des_total += b
                return
            elif a == 3:
                v = k_v.get((a, b))
                if v is None:
                    v = int(((b + 1) * b) / 2)
                    k_v[(a, b)] = v
                des_total += v
                return
            elif a > 3:  # 将行数减少
                for i in range(b, 3, -1):
                    get_count(a - 1, i)
                des_total += int((a * (a + 1)) / 2)

        get_count(m, n)
        return des_total


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(10, 38))  # 548354040
