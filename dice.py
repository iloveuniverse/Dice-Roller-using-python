import random
round=1
f1=0
f2=0
def dice_roll():
    p=random.randrange(1,6)
    return p

while round<4:
    player1=dice_roll()
    player2=dice_roll()
    print(player1)
    print(player2)

    if player1>player2:
        f1=f1+1
    else:
        f2=f2+1
    round=round+1

if f1>f2:
    print("First person won!")
else:
    print("Second person won!")
