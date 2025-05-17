filename = 'avatar.png'
index = 6
name = filename[:index]
print(f'上传文件的名称： {name}')

postfix = filename[index:]
print(f'上传文件的后缀： {postfix}')