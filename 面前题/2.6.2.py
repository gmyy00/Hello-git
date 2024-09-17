# 你有足够多的1分，2分，5分硬币，想要凑出n元钱(n为正整数)，有多少种方法？
# input  : n
# output : 不同方法的个数

# 神金解法：
"""
n = int(input())
ans = 0
for x in range(0, n+1):
    for y in range(0, int(n/2+1)):
        for z in range(0, int(n/5+1)):
            if x+2*y+5*z == n:
                ans += 1
print(ans)
"""

# 求一次不定方程的解个数
# 本质上就是 x+2y+5z=n(n已知,为正整数) 求解的个数
# 下面是好一点的解法

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1  # 凑出0分钱有一种方法（即不拿任何硬币）

for coin in [1, 2, 5]:  # 遍历所有可用的硬币面值
    for i in range(coin, n + 1):  # 从当前硬币面值开始遍历到n
        dp[i] += dp[i - coin]  # 累加使用当前硬币的方法数
print(dp[n])
