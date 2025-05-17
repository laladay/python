numstr = '0123456789'
# 从2到5开始切片，步长为1
print(numstr[2:5:1])
print(numstr[2:5])
# 截取好索引为5之前的字符串
print(numstr[:5])
# 截取从1开始前面的字符串
print(numstr[:1])
# 拷贝整个字符串
print(numstr[:])
# 调整步阶
print(numstr[::2])
# 字符串反装
print(numstr[::-1])
# 索引为负数的截取
print(numstr[-4:-1])
# 结束字符为负数
print(numstr[:-1])