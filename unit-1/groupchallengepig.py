import random

player1_totalscore = 0
player2_totalscore = 0
player1_turn_score = 0
player2_turn_score = 0


score= 0
command = " "
player_turn = 0

#Player 1 rolls the dice


#command = input ("command r to roll > ")

while (True):

    if player_turn == 0:
        command = input ("command r to roll > ")
        if command == "r":
            round_score = random.randint(1,6)
        if round_score == 1:
            player1_totalscore = 0
        else:
            player1_totalscore = player1_turn_score + roll
    else:
        player_turn = 1
    if command == "r":
        roll = random.randint(1,6)
        player1_turn_score = player1_totalscore + roll

    command = input ("Would you like to roll again? Type r, to hold type h > ")

    if command == "r":
        roll = random.randint(1,6)
        if roll == 1:
            player2_totalscore = 0
        else:
            player2_totalscore = player2_turn_score + roll
    else:
        player_turn = 1
    if command == "r":
        roll = random.randint(1,6)
        player2_turn_score = player2_totalscore + roll

    command = input ("Would you like to roll again? Type r, to hold type h > ")

print (player2_totalscore)        
        


    


'''
p1_dice = random.randint(1, 6)
p1_dice2 = random.randint(1, 6)
p2_dice = random.randint(1, 6)
p2_dice2 = random.randint(1, 6)
player1 = p1_dice + p1_dice2
player2 = p2_dice + p2_dice2

'''
