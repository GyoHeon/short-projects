import random

rsp = {'rock':(1, 0, 0), 'scissors':(0, 1, 0), 'paper':(0, 0, 1)}

def r_s_p(player, computer):
    return (player[1]*computer[2]-player[2]*computer[1]+player[2]*computer[0]-
            player[0]*computer[2]+player[0]*computer[1]-player[1]*computer[0])

def com(n):
    if n<=1: return rsp['rock']
    elif n <=2: return rsp['scissors']
    else: return rsp['paper']

def pla(word):
    if word=='rock': return rsp['rock']
    elif word=='scissors': return rsp['scissors']
    else: return rsp['paper']

p = pla(input())
c = com(random.randint(1,3))

if r_s_p(p, c) > 0:
    print('Win!')
elif r_s_p(p, c) < 0:
    print('Lose!')
else:
    print('Draw!')