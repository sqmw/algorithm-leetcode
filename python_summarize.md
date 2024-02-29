1. 唯一标识 id()/哈希值 hash()
    - 哈希值
        - hash() 函数，参数必须为不可变的，类型课`dict`的类型一样
            - hash() 函数并不是总是返回唯一的值，不同的对象可能具有相同的哈希值（哈希冲突）。哈希值是根据对象的内容计算的，相同内容的对象应该有相同的哈希值。
            - 代码表示
                ```python
              if __name__ == "__main__":
                    a = (1, 2, 3)
                    b = (1, 2, 3)
                    print(hash(a) == hash(b))  # True
                ```
    - 唯一标识
        - id() 函数，返回唯一的标识
            - 唯一标识符是在对象的生命周期中保持不变的，但它不同于哈希值
            - 代码表示1
              ```
                if __name__ == "__main__":
                   a = (1, 2, 3)
                   b = (1, 2, 3)
                   print(id(a) == id(b))  # True，可以参考常量池
              ```
            - 代码表示2
              ```
                if __name__ == "__main__":
                   a = [1, 2, 3]
                   b = [1, 2, 3]
                   print(id(a) == id(b))  # False，可以参考常量池
              ```
2. sum()
    - usage1
    ```
      if __name__ == "__main__":
         print(sum([False, False, True]))  # 1
     ```
3. set/dict
    - 在 Python 中，有类似于 Java 中的 HashSet 的集合实现，它就是 set 类型。set 是一个无序的、不重复的集合，它是基于哈希表实现的。
    - Python 的内置字典和集合在大多数情况下已经提供了高效的查找操作，但通过合理使用哈希表、控制哈希冲突等方法，可以进一步优化性能。

4. 进位置转化 bin()、oct()、hex()、int()
    - 需要理解除 n 取余法
    - 0b: binary
    - 0o: octal
    - 0x: hexadecimal
    - bin():10->2
    - oct():10->8
    - hex():10->16
    - `def bin(integer: int)->str:`
    - def int(num_str: str, radix: int) -> int(num_str: 表示的是进位置为radix的表示的数字)
5. str.ljust()/str.rjust()
    - ljust == dart: padRight(width, padding)
    - rjust == dart: padLeft(width, padding)
6. 位运算 (&/|/~/^)
