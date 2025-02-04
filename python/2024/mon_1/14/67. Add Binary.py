class Solution:
    def addBinary(self, a: str, b: str) -> str:
        des_str = ''
        carry = 0
        smaller_len = min(len(a), len(b))
        bigger_len = max(len(a), len(b))
        if bigger_len != len(a):
            t = a
            a = b
            b = t
        for i in range(bigger_len - 1, bigger_len - smaller_len - 1, -1):
            des_str = f'{(int(a[i]) + int(b[i - (bigger_len - smaller_len)]) + carry)%2}' + des_str
            carry = (int(a[i]) + int(b[i - (bigger_len - smaller_len)]) + carry) // 2
        for i in range(bigger_len - smaller_len - 1, -1, -1):
            des_str = f'{(int(a[i]) + carry) % 2}' + des_str
            carry = (int(a[i]) + carry) // 2
        if carry != 0:
            des_str = '1' + des_str
        return des_str


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('101', '111'))