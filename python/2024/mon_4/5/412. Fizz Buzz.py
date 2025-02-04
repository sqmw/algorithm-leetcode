from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        answer[i] == "Fizz" if i is divisible by 3.
        answer[i] == "Buzz" if i is divisible by 5.
        answer[i] == i (as a string) if none of the above conditions are true.
        :param n:
        :return:
        """
        answer: List[str] = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(f'{i}')
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                              "FizzBuzz"]
