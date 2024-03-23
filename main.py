class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        # 当 n >= 4 时，可以将 n 拆分为尽可能多的因子 3 和一个可能的因子 2
        # 因为 3 * 3 > 2 * 2 * 2，所以应该尽量多地拆分成因子 3
        # 如果 n 可以被 3 整除，直接返回 3 的幂次
        # 如果 n 除以 3 有余数，将余数加入到拆分中
        quotient, remainder = divmod(n, 3)
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2


