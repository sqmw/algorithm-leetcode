# LEETCODE

- 做题换算 难 = 2 * 中等 == 4 * 简单
    - 做到需要收费的时候每天 4 题及其以下
- 变量定义域的使用按照C语言使用(更加规范)
- 编写算法不仅需要保证性能，也需要保证代码的可读性
- 160题附近开始收费，此时已经做完所有的数据结构一遍了(似乎还差图，但是树也是特殊的图)
- 本人算法实现规则：
    - 时间复杂度需要达到最低
    - 空间复杂度不超过O(n)即可，对于空间复杂度的要求非必要不降低到O(1)
- 本人变量命名
    - des_XXX 表示目标值
    - rec_f 表示递归/迭代函数

## 数据结构&算法基础

- 数据结构和算法是核心
    - 排序算法需要全部能够实现
    - 需要会所有的图(线性表和二叉树都是特殊的图,字符串是特殊的线性表)
    - 需要能够手动实现一个 hash

## 算法实现

1. 循环
2. 递归

### 递归 == 循环 + 栈

*`递归和循环的S、T各不相同`*

## 算法使用的数据结构

1. 线性表
2. 字符串
3. 树
    1. 线段树(segment tree)/树状数组(Binary Indexed Tree，BIT)
4. 图

## 算法思想

1. 贪心算法

2. 动态规划
    - 一般动态规划
    - 记忆化搜索(从后往前看的递归动态规划)

    - 动态规划的本质：
        - 数学归纳法(递推公式)
        - f(x) = f(x - 1) + f(x - 2) + ...(第n项的结果由前面的某m项决定)

3. traceback(216)

```
if condition_if:
    des_arr.append(path[:])
else:
    for condition_for:
        path.append()
        traceback()
        path.pop()
```

### 贪心算法难题

| 题号  | 时间复杂度      | 题目                             | 完成方法                |
|-----|------------|--------------------------------|---------------------|
| 300 | O(nlog(n)) | Longest Increasing Subsequence |                     |
| 162 |            |                                |                     |
| 179 |            |                                | (内置排序算法，想到但是不能排序出来) |
| 334 | O(n)       | triplet                        | 两个数组最优置换            |

- 未证明可行性:
  162
- 看答案做出题:
    - 179(内置排序算法，想到但是不能排序出来)
      ```
        nums = [2, 1, 3, 4, 1, 2, 3, 4]
        def cmp(x, y):
            return x - y # -1 理解为 每次 x 取出最小的一个 x(java的比较函数就是这样)
        nums.sort(key=functools.cmp_to_key(cmp))
        print(nums)  # [1, 1, 2, 2, 3, 3, 4, 4]       
      ```
    - 322(换零钱问题,在这里需要使用记忆化搜索实现)

### 回溯思想难题

题目序号：39 78 90

### 动态规划难题

题目序号：73,139,337(二叉树的动态规划), 392(使用动态规划来理解和做是难点)

### 时间上面需要提升的题目

| 题目序号 | 题目描述                                            | 总结 |
|------|-------------------------------------------------|----|
| 105  | 需要加深二叉树 先序\|中序 遍历特性的理解                          | ?  |
| 106  | 需要加深二叉树 中序\|后序 遍历特性的理解                          | ?  |
| 130  | 广度优先遍历/二维数组                                     | ?  |
| 307  | 线段树(segment tree)/树状数组(Binary Indexed Tree，BIT) | ?  |

### 未做出来题目

| 题目序号                          | 知识点       | 总数 |
|-------------------------------|-----------|----|
| 95(3) 、 96(3)[需要做出98题再来做这两题]  | 树的遍历      | 1  |
| 241                           | 和 95 一个类型 | 2  |
| 292                           | NIM游戏和博弈论 | 3  |
| 309(多个数组动态规划)                 | 股票买卖/要冷却  | 4  |
| 310(图变树)[超时后看答案解出来的,类似找重心的过程] | 减节点/树的直径  | 5  |

### bit manipulation(位运算)

| 201 | ... | ... | ... |
|-----|-----|-----|-----|
|     |     |     |     |

### 其他

#### 数学

| 题目序号 | 题目知识                  |
|------|-----------------------|
| 204  | prime                 |
| 279  | 四平方定理                 |
| 372  | [372 super pow](#372) |

- <span id="372">372 super pow</span>
    - 涉及知识 (x * y) % m == ((x % m)*(y % m)) % m
    - 该表达式可以分类讨论得以证明，具有递归累计效果

#### 有趣的题目

| 题目序号 | 描述                  |
|------|---------------------|
| 205  | 同构字符串               |
| 207  | 图的遍历、环的判定           |
| 227  | 一般表达式求值             |
| 232  | 双栈实现队列&&T(n) = O(1) |
| 238  | productExceptSelf   |
| 241  | 表达式添加括号的不同方法        |
| 274  | 计数排序                |
| 287  | Floyd 数组重复数字判定/抽屉原理 |
| 292  | NIM游戏、博弈论           |
| 319  | 灯泡开关(brainteaser)   |

#### 二进制知识点

| 操作        | 意义                |
|-----------|-------------------|
| x&(x - 1) | 用来去除 x 的最右边的第一个 1 |

