# -*- coding: UTF-8 -*-

# Filename : set-math-homework.py
# author by : （学员ID)

# 要点：进一步掌握 for, if
# 同时掌握  !=, ==, random, file, %0.2f

import random

# 编写 n 行 m 列 的小学加减乘除测试题

# 打开题目文件清空之前内容
file1 = "math_ask.txt"
f1 = open(file1, 'w')  # 先清空文件内容
line1 = "-----小学四则运算题-----\n"
f1.write(line1)
f1.close()

# 打开答案文件清空之前内容
file2 = "math_answer.txt"
f2 = open(file2, 'w')  # 先清空文件内容
line2 = "-----小学四则运算题（含答案）-----\n"
f2.write(line2)
f2.close()

# 再次以追加方式打开文件
f1 = open(file1, 'a')  # 追加方式一次加一行
f2 = open(file2, 'a')  # 追加方式一次加一行


# 变量初始化
rows = 20        # 总行数
columns = 5     # 总列数
count = 0       # 总出题数

# 自动生成题目
# 按行数循环
for n in range(1, rows + 1):

    # 清空本行输出
    line1 = ""
    line2 = ""

    # 按列数循环
    for m in range(1, columns + 1):

        # 记录总出题数
        count += 1

        # 随机生成2个 0-99 之间的整数
        a = random.randint(0, 99)
        b = random.randint(0, 99)

        # 随机生成运算符
        op = random.randint(1, 4)

        # 生成计算式
        # 加法计算式
        if op == 1:
            line1 += "%d + %d = \t\t\t" % (a, b)
            answer = a + b
            line2 += "%d + %d = %d \t\t\t" % (a, b, answer)
        # 减法计算式 - 不能出现负数
        if op == 2:
            if a >= b:
                line1 += "%d - %d = \t\t\t" % (a, b)
                answer = a - b
                line2 += "%d - %d = %d \t\t\t" % (a, b, answer)
            else:
                line1 += "%d - %d = \t\t\t" % (b, a)
                answer = b - a
                line2 += "%d - %d = %d \t\t\t" % (b, a, answer)
        # 乘法计算式
        if op == 3:
            line1 += "%d * %d = \t\t\t" % (a, b)
            answer = a * b
            line2 += "%d * %d = %d \t\t\t" % (a, b, answer)
        # 除法计算式 - 除数不能为 0  - 扩展（不能出现份数和没法整除的数）
        # 判定表方式制作
        if op == 4:
            if a == 0 and b != 0:
                line1 += "%d ÷ %d = \t\t\t" % (a, b)
                answer = a / b
                line2 += "%d ÷ %d = %0.2f \t\t\t" % (a, b, answer)
            else:
                if b == 0 and a != 0:
                    line1 += "%d ÷ %d = \t\t\t" % (b, a)
                    answer = b / a
                    line2 += "%d ÷ %d = %0.2f \t\t\t" % (b, a, answer)
                else:
                    if a == 0 and b == 0:
                        # 重新随机生成 b 为 1-99 之间的数
                        b = random.randint(1, 99)
                        line1 += "%d ÷ %d = \t\t\t" % (a, b)
                        answer = a / b
                        line2 += "%d ÷ %d = %0.2f \t\t\t" % (a, b, answer)
                    else:
                        line1 += "%d ÷ %d = \t\t\t" % (a, b)
                        answer = a / b
                        line2 += "%d ÷ %d = %0.2f \t\t\t" % (a, b, answer)
    # 写入题目行
    line1 += "\n"
    f1.write(line1)  # 写入一行

    # 写入答案行
    line2 += "\n"
    f2.write(line2)  # 写入一行


# 总出题数
line1 = "-----结束--- 总共出了 (%d) 道四则运算题 ----" % (count)
f1.write(line1)  # 写入一行

line2 = "-----结束--- 总共出了 (%d) 道四则运算题（含答案） ----" % (count)
f2.write(line2)  # 写入一行

# 最后勿忘关闭文件
f1.close()
f2.close()
