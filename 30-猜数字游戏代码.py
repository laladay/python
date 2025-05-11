import random
i = 0
secretNum = random.randint(1, 10)
while i < 3:
    userNum = int(input('请输入您猜的数字（范围1~10之间）'))
    if secretNum == userNum:
        print('恭喜你猜对了')
        break
    elif secretNum < userNum:
        print('猜大了')
    elif secretNum > userNum:
        print('猜小了')
    i += 1

