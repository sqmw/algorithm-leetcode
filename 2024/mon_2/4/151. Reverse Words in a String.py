from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        str_list: List[str] = s.split(' ')
        str_list.reverse()
        i = 0
        while i < len(str_list):
            if str_list[i] == '':
                del str_list[i]
            else:
                i += 1
        print(str_list)
        return ' '.join(str_list)


if __name__ == "__main__":
    def example_function(*args, **kwargs):
        # args 是一个包含所有传入的位置参数的元组
        print("Positional arguments:", args)

        # kwargs 是一个包含所有传入的关键字参数的字典
        print("Keyword arguments:", kwargs)


    # 使用示例
    example_function(1, 2, 3, name='John', age=25)
