# str1 = ' '
# print(str1.isspace())
username = input('请输入您的用户名：')
if len(username) == 0 or username.isspace():
    print('您没有输入任何字符...')
else:
    print(f'您输入的字符{username}')