# -*- coding: UTF-8 -*-

# Filename : triangle.py
# author by : （学员ID)

# 判断输入的三个数字是否为正常的三角形三边长
#   如果是则计算其面积
#   如果否则输出错误信息
a = float(input('输入三角形第一边长 a=: '))
b = float(input('输入三角形第二边长 b=: '))
c = float(input('输入三角形第三边长 c=: '))

if (a + b >= c) and (a + c >= b) and (b + c >= a):
    if (abs(a - b) >= c) or (abs(a - c) >= b) or (abs(b - c) >=a):
        print("错误！某两边之差大于第三边，所以无法组成三角形。")
    else:
        print("right")
else:
    print("错误！某两边之和小于第三边，所以无法组成三角形。")


# 枚举1-10 之间，可能组成三角形的一组数
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1,10):
            if (a + b >= c) and (a + c >= b) and (b + c >= a):
                if (abs(a - b) >= c) or (abs(a - c) >= b) or (abs(b - c) >= a):
                    # print("错误！某两边之差大于第三边，所以无法组成三角形。")
                    print("", end="")
                else:
                    # print("正确！")
                    print("", end="")
            else:
                # print("错误！某两边之和小于第三边，所以无法组成三角形。")
                print("", end="")

# 枚举1-10 之间，可能组成三角形的一组数
# 如果该数组可以组成三角形，计算出其面积，并写入文件

# 打开文件准备写入
filename = "test.txt"
f = open(filename, 'w')  # 先清空文件内容
text2write = "--------清空文件行-----\n"
f.write(text2write)
f.close()

# 再次以追加方式打开文件
f = open(filename, 'a')  # 追加方式一次加一行

# 变量初始化
count = 0
text2write = ""

count_right = 0
count_error = 0

area_max = 0
area_min = 999999999999
area_total = 0

# 暴力循环尝试
for a in range(1, 100):
    for b in range(2, 200):
        for c in range(3, 300):
            count += 1
            if (a + b > c) and (a + c > b) and (b + c > a):
                if (abs(a - b) < c) and (abs(a - c) < b) and (abs(b - c) < a):
                    # 只有正确时才采取行动

                    # 计算半周长
                    p = (a + b + c) / 2

                    # 计算面积
                    # 掌握 python 开根号的写法
                    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

                    # 记录最大和最小面积的三角形
                    if area > area_max:
                        area_max = area
                    if area < area_min:
                        area_min = area

                    # 汇总所有三角形的面积
                    area_total += area

                    # 写入文件
                    text2write = "正确！第【%d】次组合，a=(%d),b=(%d),c=(%d), 面积为（%f）\n" % (count, a, b, c, area)
                    f.write(text2write)
                    count_right += 1
                else:
                    # text2write = "错误！第【%d】次组合，a=(%d),b=(%d),c=(%d)\n" % (count, a, b, c)
                    count_error += 1
            else:
                # text2write = "错误！第【%d】次组合，a=(%d),b=(%d),c=(%d)\n" % (count, a, b, c)
                count_error += 1

text2write = "--------总结行-----\n"
f.write(text2write)
text2write = "正确的组合有（%d）组， 错误的组合有（%d）组，合计尝试了（%d）组，正确的组合占比(%f)\n" % (count_right, count_error, count, count_right/count)
f.write(text2write)
text2write = "最大的三角形面积为（%f），最小的三角形面积为（%f），平均面积为（%f）\n" % (area_max, area_min, area_total/count)
f.write(text2write)

# 关闭文件
f.close()
