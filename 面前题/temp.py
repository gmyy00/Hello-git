# # c = 1.3736
# # a = int(str(c)[-5:].strip('.'))
# # print(c,a)
#
# def counter(x):
#     while 1:
#         x += 1
#         yield x

# a = counter(0)
#
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# print(a)
#
# counter = counter(0)
# n = next(counter)
# # print(f'round-{next(counter)}!')
#
# print(f'round-{n}!')

# def count_ways_to_make_change(n):
#     # 初始化一个长度为n+1的列表dp，用于存储凑出0到n分钱的方法数
#     # dp[0]初始化为1，因为凑出0分钱只有一种方法（即不拿任何硬币）
#     dp = [0] * (n + 1)
#     dp[0] = 1
#
#     # 遍历从1到n的每一个金额i
#     for i in range(1, n + 1):
#         # 初始化dp[i]为0，因为我们接下来会累加使用不同硬币的方法数
#         dp[i] = 0
#
#         # 如果i >= 1，我们可以考虑使用1分硬币
#         # dp[i-1]表示凑出i-1分钱的方法数，现在加上一个1分硬币就可以凑出i分钱
#         # 因此，dp[i]需要加上dp[i-1]
#         if i >= 1:
#             dp[i] += dp[i - 1]
#
#             # 如果i >= 2，我们可以考虑使用2分硬币
#         # 同理，dp[i-2]表示凑出i-2分钱的方法数，现在加上一个2分硬币就可以凑出i分钱
#         # 因此，dp[i]还需要加上dp[i-2]
#         if i >= 2:
#             dp[i] += dp[i - 2]
#
#             # 如果i >= 5，我们可以考虑使用5分硬币
#         # 同理，dp[i-5]表示凑出i-5分钱的方法数，现在加上一个5分硬币就可以凑出i分钱
#         # 因此，dp[i]还需要加上dp[i-5]
#         if i >= 5:
#             dp[i] += dp[i - 5]
#
#             # 遍历结束后，dp[n]就包含了凑出n元钱的不同方法数
#     return dp
#
#
# # 示例
# n = 10
# print(count_ways_to_make_change(n))  # 输出凑出10元钱的不同方法数


# def count_ways_to_make_change(n):
#     # 初始化dp列表，dp[i]表示凑出i分钱的方法数
#     dp = [0] * (n + 1)
#     dp[0] = 1  # 凑出0分钱只有一种方法（即不拿任何硬币）
#
#     # 遍历从1到n的每一个金额
#     for i in range(1, n + 1):
#         # 如果i >= 1，则可以考虑使用1分硬币
#         if i >= 1:
#             dp[i] += dp[i - 1]
#             # 如果i >= 2，则可以考虑使用2分硬币
#         if i >= 2:
#             dp[i] += dp[i - 2]
#             # 如果i >= 5，则可以考虑使用5分硬币
#         if i >= 5:
#             dp[i] += dp[i - 5]
#
#             # 返回凑出n元钱（即n分）的不同方法数
#     return dp[n]
#
#
# # 示例
# n = 3
# print(count_ways_to_make_change(n))  # 输出凑出3分钱的不同方法数，应该是2（1+1+1和1+2）

#
# def count_ways_to_make_change(n):
#     dp = [0] * (n + 1)
#     dp[0] = 1  # 凑出0分钱有一种方法（即不拿任何硬币）
#
#     for coin in [1, 2, 5]:  # 遍历所有可用的硬币面值
#         for i in range(coin, n + 1):  # 从当前硬币面值开始遍历到n
#             dp[i] += dp[i - coin]  # 累加使用当前硬币的方法数
#
#     return dp[n]
#
#
# # 示例
# n = 200
#
# print(count_ways_to_make_change(n))  # 输出应该是2（1+1+1和1+2）

# a = [1,2,3,4,5,6,7]
# b = reversed(a)
# print(b)
