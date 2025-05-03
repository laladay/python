import random

player = int(input('请输入您的出拳0 - 代表石头, 1代表剪刀，2代表布: '))
computer = random.randint(0, 2)
print(computer)

if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')

