import collections


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        两个数字的相加，用补码来相加即可，这里主要就是模拟电脑的运算
        :param a:
        :param b:
        """
        if a < 0:
            # 这个操作就是 按位取反 + 1(就是求补码)，虽然题意不让使用 +-, 但这里符合题目的考察要求
            a = 9999 - abs(a) + 1
        if b < 0:
            b = 9999 - abs(b) + 1
        a_bin_int_list = list(map(int, bin(a)[2:].zfill(14)))
        b_bin_str_list = list(map(int, bin(b)[2:].zfill(14)))
        carry = 0
        des_str_list = collections.deque()
        for i in range(13, -1, -1):
            total = carry + a_bin_int_list[i] + b_bin_str_list[i]
            carry = total >> 1
            des_str_list.appendleft(total & 1)
        des_str_list.appendleft(carry)
        des_num = int(''.join(map(str, des_str_list)), 2)
        # 移除高位
        des_num %= 10000
        return des_num if des_num <= 2000 else des_num - 10000


if __name__ == "__main__":
    s = Solution()
    print(s.getSum(-1000, -1000))
