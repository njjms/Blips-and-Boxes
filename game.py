#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import time
from pprint import pprint

print 'Blips and Boxes'
time.sleep(1)
print 'aka \'A Simulation of That Weird Section in the Navy ASVAB\''
time.sleep(2)
os.system('clear') 

print '\n'

yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

input = raw_input("Do you need instructions? (y/n) ").lower()

if input in yesChoice:
    print """This game consists of 15 questions. Each question begins with an empty board with three dashes in the center. Each dash initially represents the number 5. For each question, a number of boxes will flash sequentially above and below the dashes - if a box flashes above a dash, add one to the number of that dash. If a box flashes below that dash, subtract one from the number of that dash. At the end of the question, you will be prompted to input the numbers of each dash. You will enter these three numbers as a single number, for example 555 or 674. At the end of the game, you will be told how many questions you got correct and what the correct answers were."""

    raw_input('When you\'re done, press Enter to continue.')
    os.system('clear')

    print 'Cool. Let\'s play!'

else:
    print 'Cool. Let\'s play!'

def draw_board():
	print '|' + ''.center(7, '=') + '|'
	print '|' + ''.center(7, ' ') + '|'
	print '| - - - |'
	print '|' + ''.center(7, ' ') + '|'
	print '|' + ''.center(7, '=') + '|'

init_number = [5, 5, 5]
flash_duration = 1 
time_between_questions = 5
number_of_flashes = [5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8] 

def flash_reset():
    time.sleep(flash_duration)
    os.system('clear')
    draw_board()
    time.sleep(.1)
    os.system('clear')

def wait_for_next_question():
    os.system('clear')
    for i in range(time_between_questions): 
        print 'Next question in...' + str(time_between_questions - i)
        time.sleep(1)
        os.system('clear')

def list_to_int(numList):   # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s

def blip_one(box_goes_below):

    if box_goes_below < .5: # box should flash above
        print '|' + ''.center(7, '=') + '|'
        print '| ' + '█'.ljust(8, ' ') + '|'
        print '| - - - |'
        print '|' + ''.center(7, ' ') + '|'
        print '|' + ''.center(7, '=') + '|'
        init_number[0] = init_number[0] + 1
        flash_reset()
    else:                   # box should flash below
        print '|' + ''.center(7, '=') + '|'
        print '|' + ''.center(7, ' ') + '|'
        print '| - - - |'
        print '| ' + '█'.ljust(8, ' ') + '|'
        print '|' + ''.center(7, '=') + '|'
        init_number[0] = init_number[0] - 1
        flash_reset() 

    
def blip_two(box_goes_below):

    if box_goes_below < .5: # box should flash above
        print '|' + ''.center(7, '=') + '|'
        print '|' + '█'.center(9, ' ') + '|'
        print '| - - - |'
        print '|' + ''.center(7, ' ') + '|'
        print '|' + ''.center(7, '=') + '|'
        init_number[1] = init_number[1] + 1
        flash_reset()
    else:                   # box should flash below
        print '|' + ''.center(7, '=') + '|'
        print '|' + ''.center(7, ' ') + '|'
        print '| - - - |'
        print '|' + '█'.center(9, ' ') + '|'
        print '|' + ''.center(7, '=') + '|'
        init_number[1] = init_number[1] - 1
        flash_reset()


def blip_three(box_goes_below):

    if box_goes_below < .5: # box should flash above
        print '|' + ''.center(7, '=') + '|'
        print '|' + '█'.rjust(8, ' ') + ' |'
        print '| - - - |'
        print '|' + ''.center(7, ' ') + '|'
        print '|' + ''.center(7, '=') + '|'
        init_number[2] = init_number[2] + 1
        flash_reset()
    else:                   # box should flash below
        print '|' + ''.center(7, '=') + '|'
        print '|' + ''.center(7, ' ') + '|'
        print '| - - - |'
        print '|' + '█'.rjust(8, ' ') + ' |'
        print '|' + ''.center(7, '=') + '|'
        init_number[2] = init_number[2] - 1
        flash_reset()


raw_input('Hit Enter to start!')
os.system('clear')

correct_or_incorrect = []
correct_answers = []
your_answers = []
number_correct = 0
number_of_questions = 15

for i in range(number_of_questions):

    print 'Question ' + str(i + 1)
    time.sleep(1)
    os.system('clear')
    draw_board()
    time.sleep(1)
    os.system('clear')

    for j in range(number_of_flashes[i]):

        which_blip = random.uniform(0, 1)
        box_goes_below = random.uniform(0, 1)

        if 0 <= which_blip <= .333:
            blip_one(box_goes_below)
        elif .334 <= which_blip <= .666:
            blip_two(box_goes_below)
        else:
            blip_three(box_goes_below)
            
    raw_answer = raw_input('Type your answer now:')
    your_answers.append(raw_answer)
    correct_answers.append(list_to_int(init_number))
    
    answer = [int(k) for k in str(raw_answer)]
    
    if answer == init_number:
        correct_or_incorrect.append('Question ' + str(i + 1) + ': Correct!')
        number_correct = number_correct + 1
    else:
        correct_or_incorrect.append('Question ' + str(i + 1) + ': Wrong :(')

    os.system('clear')
    init_number = [5, 5, 5] # reset number to 555 
    
    if i < number_of_questions:
	wait_for_next_question()
    else:
	pass

os.system('clear')
print 'You made it to the end!'
print 'You got ' + str(number_correct) + ' correct out of ' + str(number_of_questions)
raw_input('Hit Enter to continue...')
os.system('clear')
pprint(correct_or_incorrect)
print 'Here were your answers: '
pprint(your_answers)
print 'And here were the correct ones: '
pprint(correct_answers)
    
