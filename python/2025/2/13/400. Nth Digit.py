class Solution:

    def __init__(self):
        """
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
        方法：可以确定数字是多少位的，然后确定是对应位里面的第几个
        0          => 0                        => 0
        10         => 0123456789               => 10 * 1 = 10
        100 - 10   => 10 11 12 13 14 15 ... 99 => (100 - 10) * 2 = 180
        1000 - 100 => 100 101 ... 999          => (1000 - 100) * 3 = 2700
        对于每一个数字 x 我们都能求出来她的前面有多少个数字出现过，这样就可以使用二分法(或者有一定的偏移量)来求解

        # arr[0]: 表示位数位 0 的及其之前总共有 arr[0] 个数字
        # arr[n]: 表示位数位 n 的及其之前总共有 arr[n] 个数字
        求的方法
        arr = [0, 10]  # 190 ...
        for i in range(2, 10):
            arr.append((10 ** i - 10 ** (i - 1)) * i + arr[-1])
        print(arr)
        """
        self.static_decimal_arr = [0, 10, 190, 2890, 38890, 488890, 5888890, 68888890, 788888890, 8888888890]

    def findNthDigit(self, n: int) -> int:
        """
        34
        0-9 10-34

        345
        0-9 10-99 100-345
        """
        # 这里实际可以使用 T(n): O(1) 实现，实际是 O(3)
        # 使用二分法
        low = 1
        high = 2 ** 31 - 1  # 经过计算可以得到其实最大就是 250954974
        while low <= high:
            mid = (low + high) // 2
            mid_first_digit_index = self.fistIndex(mid)
            mid_len = len(str(mid))
            if mid_first_digit_index <= n <= mid_first_digit_index + mid_len - 1:
                print(mid)
                return int(list(str(mid))[n - mid_first_digit_index])
            elif mid_first_digit_index > n:
                high = mid - 1
            else:
                low = mid + 1

    def fistIndex(self, x) -> int:
        """
        用来计算 x 这个数字的第一个 digit 代表的位置
        目前计算都是按照 0 作为开始来计算的
        """
        num_len = len(str(x))
        return self.static_decimal_arr[num_len - 1] + (x - 10 ** (num_len - 1)) * num_len if num_len > 1 else x


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(2 ** 31 - 1))
