# Python 相关知识总结

## 1. 唯一标识 `id()` / 哈希值 `hash()`
- **哈希值**
    - `hash()` 函数，参数必须为不可变的，类型和 `dict` 的类型一样。
    - `hash()` 函数并不是总是返回唯一的值，不同的对象可能具有相同的哈希值（哈希冲突）。哈希值是根据对象的内容计算的，相同内容的对象应该有相同的哈希值。
    - **代码示例**:
      ```python
      if __name__ == "__main__":
          a = (1, 2, 3)
          b = (1, 2, 3)
          print(hash(a) == hash(b))  # True
      ```

- **唯一标识**
    - `id()` 函数，返回唯一的标识符。
    - 唯一标识符是在对象的生命周期中保持不变的，但它不同于哈希值。
    - **代码示例 1**:
      ```python
      if __name__ == "__main__":
          a = (1, 2, 3)
          b = (1, 2, 3)
          print(id(a) == id(b))  # True，可以参考常量池
      ```
    - **代码示例 2**:
      ```python
      if __name__ == "__main__":
          a = [1, 2, 3]
          b = [1, 2, 3]
          print(id(a) == id(b))  # False，可以参考常量池
      ```

## 2. `sum()`
- **用法示例**:
  ```python
  if __name__ == "__main__":
      print(sum([False, False, True]))  # 1
  ```

## 3. `set` / `dict`
- 在 Python 中，有类似于 Java 中的 HashSet 的集合实现，它就是 `set` 类型。`set` 是一个无序的、不重复的集合，它是基于哈希表实现的。
- Python 的内置字典和集合在大多数情况下已经提供了高效的查找操作，但通过合理使用哈希表、控制哈希冲突等方法，可以进一步优化性能。

## 4. 进位制转化 `bin()`、`oct()`、`hex()`、`int()`
- 需要理解除 n 取余法。
- 0b: binary
- 0o: octal
- 0x: hexadecimal
- **函数示例**:
    - `bin(): 10 -> 2`
    - `oct(): 10 -> 8`
    - `hex(): 10 -> 16`
    - `def bin(integer: int) -> str:`
    - `def int(num_str: str, radix: int) -> int:  # num_str: 表示的是进位置为radix的表示的数字`

## 5. `str.ljust()` / `str.rjust()`
- `ljust` 相当于 Dart 的 `padRight(width, padding)`
- `rjust` 相当于 Dart 的 `padLeft(width, padding)`

## 6. 位运算 (`&` / `|` / `~` / `^`)

## 7. `min` / `max`
- 经过测试发现，如果是比较两个数字的时候，不适用 `max` 或 `min` 而是仅仅使用 `if else` 语句，性能提升了一倍。
- 同样地，减少没有必要的重复计算也能够将性能大幅度提升。

## 8. `len`
- 如果一个值可以频繁调用一个方法得到或者是可以直接获取，那么直接获取的性能会比通过方法间接获取的性能好很多。

## 9. PyPy & CPython
- 在使用 PyPy 的性能接近 JS。

## 10. `arr = [0] * 10` / `matrix = [list()]*10`
- 执行这样的代码的时候仅仅是对 `[]` 里面的内容进行浅拷贝。
- 因此，每一个 `list()` 都是同一个，所以这里是一个细节的地方。