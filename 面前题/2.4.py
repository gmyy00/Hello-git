# 每轮投两次骰子：
# 第一轮如果和数为7或11则为胜，游戏结束；
# 和数为2、3或12则为负，游戏结束；
#
# 和数为其它值则将此值作为自己的点数，继续第二轮、第三轮...
# 直到某轮的和数等于点数则取胜，若在此前出现和数为7则为负。

import time


def my_random_generator(seed_, a=1103515245, m=2 ** 32):
    c = int(str(time.time())[-5:].strip('.'))
    while 1:
        seed_ = (a * seed_ + c) % m
        yield seed_  # 暂停生成


def my_dice(seed_):
    # 先创建生成器实例！！！
    dice = my_random_generator(seed_)
    
    for i in range(3):
        next(dice)

    number1 = (next(dice) % 6) + 1
    number2 = (next(dice) % 6) + 1
    result0 = number1 + number2
    return result0, number1, number2


# def counter(x):
#     while 1:
#         x += 1
#         yield x


def first_judge(result_):

    if result_ == 7 or result_ == 11:
        print('You win!')
        quit()

    elif result_ == 2 or result_ == 3 or result_ == 12:
        print('You fail!')
        quit()

    else:
        print('Again!')
        return result_


def next_judge(point_, result_):

    if result_ == point_:
        print('You win!')
        quit()

    elif result_ == 7:
        print('You fail!')
        quit()

    else:
        print('Again!')


if __name__ == '__main__':
    point, number1, number2 = my_dice(int(input('seed: ')))
    print(f'You got {number1} and {number2}')
    first_judge(point)
    while 1:
        result, number1, number2 = my_dice(int(input('seed: ')))
        print(f'You got {number1} and {number2}, the point is {point}.')
        next_judge(point, result)


