import random

rsp = {'rock':(1, 0, 0), 'scissors':(0, 1, 0), 'paper':(0, 0, 1)}

def r_s_p(player, computer):
    return (player[1]*computer[2]-player[2]*computer[1]+player[2]*computer[0]-
            player[0]*computer[2]+player[0]*computer[1]-player[1]*computer[0])

state = 0
while True:
    player = input()
    com = random.choice(['rock', 'scissors', 'paper'])
    print('Your pick :', player , "\nComs pick :", com)
    p = rsp[player]
    c = rsp[com]
    if state == 1:
        if r_s_p(p, c) > 0:
            print("Your turn!")
            state = 1
        elif r_s_p(p, c) < 0:
            print("Computer's turn!")
            state = -1
        else:
            print("You Win!")
            break
    else:
        if r_s_p(p, c) > 0:
            print("your turn!")
            state = 1
        elif r_s_p(p, c) < 0:
            print("Computer's turn!")
            state = -1
        elif r_s_p(p, c) == 0 and state == 0:
            print('Draw! again!')
        else:
            print("You lose!")
            break