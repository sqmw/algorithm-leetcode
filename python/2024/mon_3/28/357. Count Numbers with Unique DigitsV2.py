from typing import List


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1  # 只有一个数字有0位数，即0本身
        rec_f: List[int] = [10, 81]
        for i in range(3, min(n + 1, 11)):
            rec_f.append(rec_f[-1] * (10 - i + 1))

        return sum(rec_f[:n])


if __name__ == "__main__":
    print(Solution().countNumbersWithUniqueDigits(2))
