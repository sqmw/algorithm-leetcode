class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        T(n): O(n)
        S(n): T(1)
        :param s:
        :return:
        """
        absent_times: int = 0
        now_consecutive_late_times: int = 0
        max_consecutive_late_times: int = 0
        for char in s:
            if char == "L":
                now_consecutive_late_times += 1
            else:
                max_consecutive_late_times = max(max_consecutive_late_times, now_consecutive_late_times)
                now_consecutive_late_times = 0
                if char == "A":
                    absent_times += 1
        max_consecutive_late_times = max(max_consecutive_late_times, now_consecutive_late_times)
        return absent_times < 2 and max_consecutive_late_times < 3

if __name__ == "__main__":
    s = Solution()
    print(s.checkRecord('PPALLL'))
