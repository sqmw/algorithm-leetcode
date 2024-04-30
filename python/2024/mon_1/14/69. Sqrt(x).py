class Solution:
    # 使用二分法
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1
        else:
            l = 0
            r = x
            start_val = int((l + r) / 2)
            while True:
                if start_val * start_val <= x <= (start_val + 1) * (start_val + 1):
                    if x == (start_val + 1) * (start_val + 1):
                        return start_val + 1
                    return start_val
                else:
                    if start_val * start_val > x:
                        r = start_val
                    else:
                        l = start_val
                    start_val = int((l + r) / 2)



if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(9))

