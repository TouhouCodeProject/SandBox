"""
Main project file
"""
"""This program or a mini-game is designed when you don’t have anyone to play or you are under lockdown alone. 
There are a number of functions that this program requires so let us have an overview of each.

    a random function: to generate rock, paper, or scissors. 
    valid function: to check the validity of the move.
    result function: to declare the winner of the round.
scorekeeper: to keep track of the score.
The program requires the user to make the first move before it makes one the move. Once the move is validated the 
input is evaluated, the input entered could be a string or an alphabet. After evaluating the input string a winner is 
decided
by the result function and the score of the round is updated by the scorekeeper function. 
"""
import random
# Rock = 1
# Paper = 2
# Scissors = 3

def randFunc():
    """
    Rand # generating func
    :return: int
    """
    return random.randint(1,3)

def validFunc(com, human):
    """
    Validation func compare the result with com and human
    :param com: int,
    :param human: int,
    :return: str
    """
    if com == human:
        return 'Duce'
    # Com win
    elif (com == 3 and human == 2 )or (com == 2 and human == 1) or (com == 1 and human == 3):
        return 'Com win'
    else:
        return 'Human win'

def resultsFunc(results):
    print(results)

def scoreFunc(results):
    """
    Score func to memorise the socres
    :param results: str
    :return: str
    """
    global comScore
    global humanScore
    if results =='Duce':
        pass
    elif results == 'Com win':
        comScore +=1
    elif results == 'Human win':
        humanScore +=1
    return ('Computer score {0}, Human score {1}'.format(comScore, humanScore))

if __name__ == '__main__':
    comScore = 0
    humanScore = 0
    while True:
        human = int(input('Please put a number, 1 = R, 2 = P, 3 = S\n'))
        com = randFunc()
        print(com)
        results = validFunc(com, human)
        resultsFunc(results)
        print(scoreFunc(results))