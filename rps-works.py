#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def PickWinner(player, opponent):
    if player is opponent:
        return None
    elif (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player =='p' and opponent == 'r'):
        return True
    else:
        return False

def Game(count, pwins):
    if count == 1:
        play = input("Would you like to play? Enter 'y' for yes and 'n' for no")
    elif count > 1:
        play ='y'
    
    while play not in 'yn':
        play = input("Sorry, I only understand 'y' for yes and 'n' for no. Try again?")
        
    if (play == 'y'):
        player = input("Type 'r' for rock, 'p' for paper, or 's' for scissors")
        options = ('r', 's', 'p')
        while player not in options:
            player = input("Sorry? Try again. Type 'r' for rock, 'p' for paper, or 's' for scissors")
        #pick for computer
        import random
        opponent = random.choice('rsp')
        print ('You picked {}. I picked {}'.format(player,opponent))
        
        # pick a winner and update the counts
        if PickWinner(player, opponent) is True:
            pwins +=1
            print('You win!')
        elif PickWinner(player, opponent) is False:
            print ('I win!')
        else:
            print ("It's a tie!")
        
        
        print ('You\'ve won {} out of {} games.' .format(pwins, count))
    
        play = input ("Would you like to play again? 'y' for yes and 'n' for no")
        if play == 'y':
            count +=1
            Game(count, pwins)
        elif play == 'n':
            play = 'n'
            print('thanks for playing. bye')
   
    else:
        print ('okay , bye')

pwins = 0
count = 1
Game(count, pwins)
