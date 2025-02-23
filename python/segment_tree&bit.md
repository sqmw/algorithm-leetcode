# 线段树(segment tree)&BIT(binary indexed tree)
## 特点
1. 递归定义
2. 区间表示
3. 高效查改(T(n) = O(log(n)))
## 作用
1. BIT 和 segment tree 都是用来优化对数组的操作的
2. 可以用来加速求某段的总和 query
3. 同时更新也比较方便 update
## BIT
1. BIT tree[i] 表示 [i - lowbit(i) + 1, i] 上面数组的和(这里的索引是从1开始)
2. update[i] 的时候需要更新对应的 [i - lowbit(i) + 1, i] 区间相关的元素
3. 查询的时候直接查询即可
4. 不需要初始化 tree，可以通过调用 update 即可实现

## segment tree
1. 线段树功能比 BIT 强大，代码也更加复杂，需要占用的额外空间也更多
2. 可以用来，区间求和，更新，求极值
3. segment tree的结构