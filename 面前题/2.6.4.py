# input  : n -> 99，代表位数
#        : x -> 第一个 n 位的数字
#        : y -> 第二个 n 位的数字
# output : 相乘结果
import sys

n = int(input('位数：'))

x = int(input(f'请输入{n}位的正整数：'))
if len(str(x)) != n or x <= 0:
    sys.exit(f'{x}不是{n}位正整数！')

y = int(input(f'请输入{n}位的正整数：'))
if len(str(y)) != n or y <= 0:
    sys.exit(f'{y}不是{n}位正整数！')

print(x*y)
