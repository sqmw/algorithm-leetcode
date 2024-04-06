def cubic_root(a, epsilon=1e-6, max_iterations=100):
    x = a / 3  # 初始估计值，可以选择 a / 3 或其他合适的值
    for _ in range(max_iterations):
        x_next = (2 * x + a / (x ** 2)) / 3  # 牛顿迭代法的迭代公式
        if abs(x_next - x) < epsilon:
            return x_next
        x = x_next
    return x  # 返回近似的三次方根


# 示例用法
a = 2
root = cubic_root(a)
print(f"The cubic root of {a} is approximately: {root}")
