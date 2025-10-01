import random
Game = ['rock','paper','sciss']

compter = ' '

you_point=0
computer_point=0
 
Game_bet= True

while(Game_bet):
    you = input("choose (rock,paper,sciss): ")

    if you=="0":
        Game_bet=False
        
    rand= random.randint(0,2)
    computer = Game[rand]

    if you == 'rock' and computer == 'paper':
        computer_point=computer_point + 1
    if you == 'rock' and computer == 'sciss':
        you_point=you_point + 1

    if you == 'paper' and computer == 'rock':
        you_point=you_point + 1
    if you == 'sciss' and computer == 'rock':
        computer_point=computer_point + 1

    if you == 'paper' and computer == 'sciss':
        computer_point=computer_point + 1
    if you == 'sciss' and computer == 'paper':
        you_point=you_point + 1

    print("YOU: (", you_point ,")",   you  ,'- ' ,"COM: (", computer_point ,")", computer )
    if you_point>=3 or computer_point>=3:
        Game_bet = False

if you_point > computer_point:
    print("YOU WIN!")
else:
    print("YOU LOSE ):")
     
print("YOU: ",you_point)
print("COM: ",computer_point)