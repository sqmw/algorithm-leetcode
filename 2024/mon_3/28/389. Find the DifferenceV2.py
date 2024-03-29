from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        method1: 使用 hash 实现
        使用 hash 的方式来做(字母的数量是一个常数，并且字母的顺序是一定的，其实我们知道的常识一般也是有序的)
        T(n): O(n) # 2 * n +1
        S(n): O(1)
        method2： 使用疑惑操作实现
        T(n): O(n)
        S(n): O(1)
        """
        des_num = 0
        i = 0
        while i < len(s):
            des_num ^= ord(s[i])
            des_num ^= ord(t[i])
            i += 1
        des_num ^= ord(t[i])
        return chr(des_num)


if __name__ == "__main__":
    solution = Solution()
    s = "abcd"
    t = "abcde"
    print(solution.findTheDifference(s, t))
