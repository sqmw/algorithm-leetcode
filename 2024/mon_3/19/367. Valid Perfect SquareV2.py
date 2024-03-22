class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        T(n): O(log(n))
        S(n): O(1)
        """
        if num == 1:
            return True
        left = 1
        right = num // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(5))
