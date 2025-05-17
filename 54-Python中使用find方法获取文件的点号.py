filename = input('请输入您要上传文件的名称： ')
# 获取点号的索引下标
index = filename.find('.')
print(index)
# 文件名称
print(filename[:index])
print(filename[index:])