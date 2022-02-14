# 가위바위보
import random
b = ['가위', '바위', '보', '가위']
print('가위바위보를 실행합니다.')
print()

while(True):
    a = input('당신은 무엇을 내실건가요? (가위, 바위, 보)중에 골라주세요.')
    c = random.randrange(0, 3)

    if a not in b:
        print('오타가 있습니다. 다시 입력하여 주십시오.')

    else:
        print('당신은', a, '를 냈습니다.')
        print('인공지능이', b[c], '를 냈습니다.')
        print()
        if a == b[c]:
            print('비겼습니다. 게임을 다시 진행해주세요.')
        elif a == b[c + 1]:
            print('당신은 승리하였습니다.')
            break
        else:
            print('당신은 패배하였습니다.')
            break