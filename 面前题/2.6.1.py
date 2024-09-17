# “哇数学可真是太难了，我刚学完分数化简，可是看到：1428571 / 2857142这种分式就头大，还好大佬教了我怎么做，只要用约分就好了！
# 把分子分母相同的数字全部约掉，也就是把分母的 857142 和分子的 428571 划掉，数学，真是奇妙呢！”
# 补充说明：分子分母只要是相同数字即可一对一划掉，若存在一对多情况，从后往前消除
# （如题中所给例子分母只有一个 1，相对应分子消除的 1 为最后一位个位数上的 1）
# ⭐️⭐️⭐️ 尝试写一个程序得到足够多个这样的大分式
# （不需要完全正确，但你应该理解自己所写的程序是如何运作的，并有足够清晰的注释）
# 最后，你要将你的答案保存。到面试时，现场运行进行展示。
# 加分项： 将你的产出，推送到在 git 题中，创建的仓库的 dev 或主分支中。

# 神奇の142857

denominator = list(reversed(input('分母：')))
numerator = list(reversed(input('分子：')))

a0 = ''.join(reversed(denominator))
b0 = ''.join(reversed(numerator))
# 对分母的每个字符进行从后往前的遍历，在分子遇到相同的就删除，并转到分母的下一个字符
# 时间复杂度为O(n^2)
for d_index, d in enumerate(denominator):
    for n_index, n in enumerate(numerator):
        if d == n:
            denominator[d_index] = ''
            numerator[n_index] = ''
            break

a = ''.join(reversed(denominator))
b = ''.join(reversed(numerator))

print(f'约分前：{b0}/{a0}')
print(f'约分后：{b}/{a}')

# 蚌埠住了，全是reversed
