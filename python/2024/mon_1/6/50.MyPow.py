class Solution:
    def myPow(self, x: float, n: int) -> float:
        product = 1
        if n < 0:
            n = -n
            x = 1 / x
        if n == 0 or x == 1.0:
            return 1
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            half = self.myPow(x, n // 2)
            return x * half * half


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(1.0000000000001, -2147483648))
