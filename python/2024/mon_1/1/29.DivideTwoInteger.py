class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        dividend_positive = True
        divisor_positive = True
        if dividend < 0:
            dividend_positive = False
            dividend = -dividend
        if divisor < 0:
            divisor_positive = False
            divisor = -divisor
        # 100000
        carry = 10 ** 5
        quotient = 0
        while dividend >= divisor:
            if carry == 3:
                pass
            if dividend - divisor * carry >= 0:
                dividend -= divisor * carry
                quotient += 1 * carry
            # 这里的carry减少的if else可以通过一个函数表示从而优化代码
            else:
                if carry > 10**2:
                    carry /= 10
                elif carry > 50:
                    carry -= 5
                elif carry > 1:
                    carry -= 1
                # 此时 carry == 1
                else:
                    dividend -= divisor * carry
                    quotient += 1 * carry

        # 结果是正数
        if (dividend_positive and divisor_positive) or (not dividend_positive and not divisor_positive):
            if quotient > 2 ** 31 - 1:
                return 2**31 - 1
        else:
            quotient = -quotient
            if quotient < - 2**31:
                return -2**31
        # 结果是负数
        return int(quotient)


if __name__ == '__main__':
    s = Solution()
    print(s.divide(-10, 4))

