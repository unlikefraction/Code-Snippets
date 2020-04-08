import turtle
import math
import random
import time

mover = turtle.Turtle()
mover.pensize(3)
colors = ['#4287f5', '#eb8b15', '#db271a', '#1abd74', '#14b5b5', '#8b16b5', '#e01979']
mover_pos = [0, 0]
loop = True
exit_words = ['exit', 'end', 'quit', 'escape', 'finish']
allowed_words = ['up', 'down', 'left', 'right'] + exit_words

while loop:
    mover.color(random.choices(colors))
    correct_word = False
    while not correct_word:
        user_move = input('Enter the Direction or exit to quit: ').lower()
        if user_move in allowed_words:
            correct_word = True
        else:
            print('ENTER A VALID COMMAND TO EXECUTE!')
    if user_move in exit_words:
        mover.pensize(5)
        mover.color('#000000')
        mover.setpos(0, 0)
        loop = False
        break

    else:
        user_step = int(input(f'How much to Move in {user_move} direction: '))

        if user_move == 'left':
            mover_pos[0] -= user_step

        elif user_move == 'right':
            mover_pos[0] += user_step

        elif user_move == 'up':
            mover_pos[1] += user_step

        elif user_move == 'down':
            mover_pos[1] -= user_step

        mover.setpos(mover_pos[0], mover_pos[1])

# Calculate the Distance
a, b = (mover_pos[0], mover_pos[1])
final_distance = math.sqrt(a**2 + b**2)
print(f'Final Distance is {final_distance}.')

# Formula: (a^2 + b^2)^1/2 = c
time.sleep(5)
turtle.done()
