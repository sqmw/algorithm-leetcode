from typing import Set


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        method1: 1.一个算法无论是什么类型的，一定都是有边界的，
                 2. 因为这里是指数函数，因为边界更加明显，数字的数量也更加少
                 3. 直接将所有的 4 的倍数的数字放在一个 set 里面，判别的速度就是 O(1)
        T(n): O(1)
        S(n): O(1)
        """
        return n in {64, 1, 256, 1024, 4, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456,
                     1073741824, 16}


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfFour(1))

    i = 1
    while i < 2 ** 31:
        print(s.isPowerOfFour(i))
