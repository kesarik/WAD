"""
def printboard(xstate,ostate):
    zero="x" if xstate[0] else("o" if ostate[0] else 0) #If the first cell of the board (indexed as 0) is marked by X (xState[0] is true), set zero to "X".
    one="x" if xstate[1] else("o" if ostate[1] else 1)
    two="x" if xstate[2] else("o" if ostate[2] else 2)
    three="x" if xstate[3] else("o" if ostate[3] else 3)
    four="x" if xstate[4] else("o" if ostate[4] else 4)
    five="x" if xstate[5] else("o" if ostate[5] else 5)
    six="x" if xstate[6] else("o" if ostate[6] else 6)
    seven="x" if xstate[7] else("o" if ostate[7] else 7)
    eight="x" if xstate[8] else("o" if ostate[8] else 8)
    print(f" {zero} | {one} | {two}")
    print(f"---|---|---")
    print(f" {three} | {four} | {five}")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight}")

def sum(a,b,c):
    return a+b+c

def checkwin(xstate,ostate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("X Won the match")
            return 1
        if(sum(ostate[win[0]],ostate[win[1]],ostate[win[2]])==3):
            print("0 Won the match")
            return 0
    return -1

print("Welcome to Tic-Tac-Toe game")
xstate=[0,0,0,0,0,0,0,0,0]
ostate=[0,0,0,0,0,0,0,0,0]
turn=1
moves=0
while(True):
    printboard(xstate,ostate)
    if(turn==1):
        print("Chance of X:")
        value=int(input("Enter a number:"))
        xstate[value]=1
    else:
        print("Chance of O:")
        value=int(input("Enter a number:"))
        ostate[value]=1
    cwin=checkwin(xstate,ostate)
    moves+=1
    if(moves==9):
        print("Match Drag")
    
    if(cwin!=-1):
        print("match over")
        break
    turn=1-turn # Switch to player O's turn
"""

def printboard(xstate,ostate):
    zero="x" if xstate[0] else("o" if ostate[0] else 0)
    one="x" if xstate[1] else("o" if ostate[1] else 1)
    two="x" if xstate[2] else("o" if ostate[2] else 2)
    three="x" if xstate[3] else("o" if ostate[3] else 3)
    four="x" if xstate[4] else("o" if ostate[4] else 4)
    five="x" if xstate[5] else("o" if ostate[5] else 5)
    six="x" if xstate[6] else("o" if ostate[6] else 6)
    seven="x" if xstate[7] else("o" if ostate[7] else 7)
    eight="x" if xstate[8] else("o" if ostate[8] else 8)
    print(f" {zero} | {one} | {two}")
    print(f"---|---|---")
    print(f" {three} | {four} | {five}")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight}")
   
def sum(a,b,c):
    return a+b+c

def checkwin(xstate,ostate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("X won")
            return 1
        if(sum(ostate[win[0]],ostate[win[1]],ostate[win[2]])==3):
            print("O won")
            return 0
    return -1

print("Welcome to tic-tac-toe game")
xstate=[0,0,0,0,0,0,0,0,0]
ostate=[0,0,0,0,0,0,0,0,0]
turn=1
moves=0
while(True):
    printboard(xstate,ostate)
    if(turn==1):
        print("Chance of X:")
        value=int(input("Enter a number:"))
        xstate[value]=1
    else:
        print("Chance of O:")
        value=int(input("Enter a number:"))
        ostate[value]=1
    cwin=checkwin(xstate,ostate)
    moves+=1
    if(moves==9):
        print("Match Drag")
        break
    if(cwin!=-1):
        print("match over")
        break
    turn=1-turn

    
    