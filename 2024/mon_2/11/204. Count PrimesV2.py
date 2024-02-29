from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        prime_list: List[int] = [2]
        # 每次取出一个数字
        for item in range(3, n):
            is_prime = True
            boundary_val = prime_list[len(prime_list) - 1]
            # 判断这个数字是不是 Prime
            for i in range(0, len(prime_list)):
                if item % prime_list[i] == 0:
                    is_prime = False
                    break
                else:
                    if prime_list[i] >= boundary_val:
                        break
                    boundary_val = item / prime_list[i]
            if is_prime:
                prime_list.append(item)

        return len(prime_list)


if __name__ == "__main__":
    s = Solution()
    print(s.countPrimes(5000000))
