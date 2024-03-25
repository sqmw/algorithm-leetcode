# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    """
    通过 target - guess 得到
    :param num:
    :return:
    """
    return 9 - num


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        使用二分发实现
        T(n): O(log(n))
        S(n): O(1)
        """
        left = 1
        right = n
        mid = (left + right) // 2
        while left <= right:
            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
        return mid


if __name__ == "__main__":
    s = Solution()
    print(s.guessNumber(100))
