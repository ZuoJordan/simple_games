#剪刀石头布
import random 
import time
print('加载中')

hands = ('石头','剪刀','布')
rule = {
'石头':{'剪刀':'赢','布':'输'},
'剪刀':{'石头':'输','布':'赢'},
'布':{'剪刀':'输','石头':'赢'}
}
def game1():
    time.sleep(1)
    while True:

        choice = input('打1游戏规则，打2开始游戏，打3查看记录，打4结束游戏\n')
        if choice == '1':
            print('游戏规则：\n电脑随机出手，玩家需要在电脑出手后选择出石头剪刀还是布。游戏结束后，会有结果出现')

        elif choice == '2':
            print('游戏开始')
            print('-------------------------------------------------------------------------------------')

            time.sleep(1)
            print('对手正在出手...')
            hand_computer = random.choice(hands)

            time.sleep(1)
            print('对手已经出好\n到你了！')
            hand_player = input('请选择石头剪刀或布\n')

            if hand_player == hand_computer:
                print('平手')

            elif hand_player == '剪刀' or hand_player == '石头' or hand_player == '布':
                time.sleep(1)
                print ('你'+rule[hand_player][hand_computer]+'了')
                if rule[hand_player][hand_computer] == '赢':
                    with open(r"C:\Users\lenovo\Desktop\剪刀石头布游戏结果.txt",'r',encoding = 'utf-8') as result:
                        result_read = int(result.read())
                    with open(r"C:\Users\lenovo\Desktop\剪刀石头布游戏结果.txt",'w',encoding = 'utf-8') as result:
                        term_result = str(result_read + 1)
                        result.write(term_result)
                elif rule[hand_player][hand_computer] == '输':
                    with open(r"C:\Users\lenovo\Desktop\剪刀石头布游戏结果.txt",'r',encoding = 'utf-8') as result:
                        result_read = int(result.read())
                    with open(r"C:\Users\lenovo\Desktop\剪刀石头布游戏结果.txt",'w',encoding = 'utf-8') as result:
                        term_result = str(result_read - 1)
                        result.write(term_result)
                pass
            
            else:
                print('这是啥？')
                print('请重试！')
                pass
            pass
        
        elif choice == '3':
            with open(r"C:\Users\lenovo\Desktop\剪刀石头布游戏结果.txt",'r',encoding = 'utf-8') as result:
                result_read = result.read()
                print('你现在得分是：'+result_read)
            pass
        
        elif choice =='4':
            time.sleep(1)
            print('已退出！')
            break

        else:
            print('我好像不太明白你的意思，请重试。')
            pass
game1()
    
        
