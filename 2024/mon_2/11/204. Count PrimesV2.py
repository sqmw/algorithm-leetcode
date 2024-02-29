import math

class Solution:
    def countPrimes(self, n: int) -> int:
        """
        S(n): O(1)
        T(n): O(n**1.5): 还是不能通过
        :param n:
        :return:
        """

        def is_prime(val: int):
            if int(val ** 0.5) ** 2 == val:
                return False
            for i in range(2, int(math.ceil(val ** 0.5))):
                if val % i == 0:
                    return False
            return True

        if n <= 2:
            return 0
        elif n == 3:
            return 1
        prime_cou = 2
        # 每次取出一个数字
        for item in range(4, n):
            prime_cou += is_prime(item)

        return prime_cou


if __name__ == "__main__":
    s = Solution()
    print(s.countPrimes(10))
