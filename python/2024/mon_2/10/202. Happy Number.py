from typing import Set


class Solution:
    def isHappy(self, n: int) -> bool:
        n = abs(n)
        val_set: Set = set()
        while n not in val_set:
            if n == 1:
                return True
            val_set.add(n)
            n_str = str(n)
            n = 0
            for item in n_str:
                n += int(item) * int(item)

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(7))
