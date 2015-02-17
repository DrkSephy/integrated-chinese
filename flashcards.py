# coding: utf8
import random
import argparse
import sys
import os
from random import randrange, sample

def filterCards(cards, filters):
    l = []
    for c in cards:
        insert = True
        for f,v in filters:
            if str(c[f]) not in v:
                insert = False
                break
        if insert:
            l.append(c)

    return l

def selectWord(deck, filters):
    cards = filterCards(deck['cards'], filters)
    choice = random.randint(0, len(cards) - 1)
    print '-'*40
    print (deck['name'] + ' Word of the Day').center(40)
    print '-'*40

    longest = max(len(f) for f in deck['fields'])

    for f in deck['fields']:
        v = cards[choice][f]
        if type(v) not in [str, unicode]:
            v = str(v)
        print f.title().ljust(longest) + '\t' + v.encode('utf-8')

def randomInsert(list, item):
    list.insert(randrange(len(list)+1), item)

def quizRunner(deck, filters):
    print '-'*40
    print (deck['name'] + ' Quiz').center(40)
    print '-'*40
    print '\n'
    print 'Enter a number and press [ENTER] to select a choice!'
    print 'Press q to quit at any time.'
    print '\n'

    # Randomize list of problems
    # Problems will be randomly chosen from that chapter
    cards = filterCards(deck['cards'], filters)
    problemList = random.sample(range(0, len(cards)), len(cards))
    problemNum = 1
    numCorrect = 0
    numWrong = 0
    exit = False
    #print randomList
    for problem in problemList:
        # Get list of choices to display
        choices = random.sample(range(0, len(cards)), 4)
        # If there is a duplicate, replace it
        if problem in choices:
            choices[choices.index(problem)] = problem
        else:
            randIndex = randrange(0, len(choices))
            choices[randIndex] = problem
        # print "The right answer is: " + str(choices.index(problem))
        # Print headers
        print '-'*40
        print ('Problem # ' + str(problemNum)).center(40)
        print '-'*40
        print '\n'
        print 'Word: ' + cards[problem][deck['quizFormat'][0]]
        print '\n'

        for choice in choices:
            print '[' +  str(choices.index(choice)) + ']' + ':' + ' '  + cards[choice][deck['quizFormat'][1]]
        print '\n'

        while True:
            playerChoice = raw_input('Which translation is correct? ')
            if playerChoice == 'q':
                exit = True
                break
            else:
                if playerChoice == '':
                    print 'You did not select one of the choices above. Please try again.'
                else: 
                    playerChoice = int(playerChoice)
                    if playerChoice > 3:
                        print 'You did not select one of the choices above. Please try again.'
                    else:
                        break
        # Exit program
        if exit:
            break

        print '\n'
        if cards[choices[playerChoice]][deck['quizFormat'][1]] == cards[problem][deck['quizFormat'][1]]:
            print '\033[92mCorrect!\033[0m'
            numCorrect += 1
        else:
            print '\033[91mNot quite...the correct answer was: ' + cards[problem][deck['quizFormat'][1]] + '\033[0m'
            numWrong += 1
        print '\n'
        problemNum += 1
    print '\033[92mYou got ' + str(numCorrect) + ' right!\033[0m'
    print '\033[91mYou got ' + str(numWrong) + ' wrong....\033[0m'

if __name__ == '__main__':
    try:
        deckPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'decks', sys.argv[-1] + '.py')
        namespace = {}
        execfile(deckPath, namespace)
        deck = namespace['deck']
    except:
        deckPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'decks')
        print "Unrecognized deck.  Available decks:"
        for f in os.listdir(deckPath):
            print f.split('.')[0]
        exit()

    parser = argparse.ArgumentParser(description='Select a chapter.')
    parser.add_argument('--quiz', help='Enter interactive quiz mode?', action='store_true')

    for f in deck['filters']:
        parser.add_argument('--' + f)

    kwargs, args = parser.parse_known_args()
    if kwargs.quiz:
        quizRunner(deck, [(f, vars(kwargs)[f].split(',')) for f in deck['filters'] if vars(kwargs)[f]])
    else:
        selectWord(deck, [(f, vars(kwargs)[f].split(',')) for f in deck['filters'] if vars(kwargs)[f]])