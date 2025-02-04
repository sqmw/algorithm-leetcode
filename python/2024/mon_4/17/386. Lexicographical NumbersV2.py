from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        method1: 生成之后排序
            T(n): O(nlog(n))
            S(n): O(n)
        method2: 直接按照规则生成(套娃)
            T(n): O(n)
            S(n): O(n)
        """

        def dic_num_generator(base: int):
            nonlocal des_nums
            if len(des_nums) >= n or base > n:
                return
            for i in range(0, 10):
                # 扩展一个位
                candidate = base * 10 + i
                if candidate <= n:
                    des_nums.append(candidate)
                    dic_num_generator(candidate)
                else:
                    break

        des_nums = []
        for i in range(1, 10):
            if i <= n:
                des_nums.append(i)
                dic_num_generator(i)
        return des_nums


if __name__ == "__main__":
    s = Solution()
    print(s.lexicalOrder(13))
