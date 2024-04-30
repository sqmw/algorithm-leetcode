from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        """
        _total_time: int = 0
        # 表示不包含
        last_stop = 0
        for i in range(len(timeSeries)):
            if timeSeries[i] < last_stop:
                _total_time -= (last_stop - timeSeries[i])
            _total_time += duration
            last_stop = timeSeries[i] + duration
        return _total_time


if __name__ == "__main__":
    s = Solution()
    print(s.findPoisonedDuration([1, 4], 2))
