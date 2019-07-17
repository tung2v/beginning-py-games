#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/



def pickCode():
    '''
    Randomly generates a 4-color code the user has to guess.
    '''
    import random
    colors = ('b', 'r', 'y', 'g', 'w', 'p')
    goal = tuple( random.choices (population = colors, k= 4))
    return goal


def GetA(cguess, cgoal):
    '''
    Adds 'a' to results for exact matches in goal and guess lists.
    '''
    result = []
    x = 0
    for x in range(4):
        if cguess[x] == cgoal [x]:
            result.append ('a')
            cgoal[x] = ' '
            cguess[x] = '-'
            #for testing
            #print ('goal is now {}'.format(cgoal))
    return result, cguess, cgoal

def GetZ(cguess, cgoal, turns):
    '''
    Adds 'z' to results for matches in color but not placement in goal and guess lists. Returns the whole result as a list.
    '''
    middleStep = GetA(cguess, cgoal)
    result = middleStep[0]
    cguess = middleStep[1]
    cgoal = middleStep[2]
    turns += 1
    q = 0
    for q in range(4):
        if cguess[q] in cgoal:
            result.append('z')
            #for testing
            #print ('same color, wrong space is {}'.format(cguess[q]))
    return result, turns
        

def main():
    '''
    Plays the game! Gives user 6 guesses. i definitely did not even give the color options tho lol
    '''
    turns = 0
    userResult = []
    goal = pickCode()
    #just for tests
    #print (goal)
    
    while (turns < 6) and (userResult != ['a', 'a', 'a', 'a']):
        guess = tuple( input ('take a guess!'))
        print ("your guess is {}" .format(guess))
        
        cguess = list(guess)
        cgoal = list(goal)
        
        processed = list(GetZ(cguess, cgoal, turns))
        userResult = processed[0]
        print ('the result of your guesses is {}'.format(userResult))
        turns = processed[1]
        print ('you\'ve used {} turns'.format(processed[1]))
    if userResult == ['a', 'a', 'a', 'a']:
        print('congrats! you cracked it')
    else:
        print ('sorry, you took too many guesses. the code was {}'.format(goal))




if __name__ == '__main__': main()