"""
end=''：不换行，接着输出。

end=' '：输出后添加一个空格。

end='\n'：默认行为，输出后换行。
"""
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print("* ", end='')
        j += 1
    print('')
    i += 1
