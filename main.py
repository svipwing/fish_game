import random,time

fish = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    ['0','1','2','3','4']
]

for i in range(len(fish)-1):
    fish[i][random.randint(0,4)] = '鱼'

print("吃掉小鱼游戏")
print("v2.0.0")
print("三秒后自动开始游戏")

time.sleep(3)

while True:
    for i in fish:
        print(i)
    
    start = time.time()
    a = int(input())
    end = time.time()
    
    if end-start > 2:
        print('反应太慢了，超时！')
        break

    if a<len(fish[-2]):
        if fish[-2][a]=='鱼':
            print('答对了')
        else:
            print('答错了')
            break
    else:
        print('超出范围')
        break
        
    fish.insert(0,[' ',' ',' ',' ',' '])
    fish[0][random.randint(0,4)] = '鱼'
    fish.pop(-2)