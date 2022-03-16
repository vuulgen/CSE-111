

print('''This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.''')
import math
total = 0
positive=''
negative=''

def input_question(answer, question, total):
    print('Enter D, d, a, or A: ')
    return answer, total 


if positive == 'D' or 'd' or 'a' or 'A':
    if positive == 'D':
        total += 0
    elif positive == 'd':
        total += 1
    elif positive =='a':
        total += 2
    elif positive == 'A':
        total += 3
elif negative == 'D' or 'd' or 'a' or 'A':
    if negative =='D':
        total -= 3


    return total


positive = print('''1. I feel that I am a person of worth, at least on an
equal plane with others.''')
input_question (positive, negative, total)

positive = print('2. I feel that I have a number of good qualities.')
input_question (positive, negative, total)

negative = print('3. All in all, I am inclined to feel that I am a failure.')
input_question (positive, negative, total)

positive = print('4. I am able to do things as well as most other people.')
input_question (positive, negative, total)

negative = print('5. I feel I do not have much to be proud of.')
input_question (positive, negative, total)

positive = print('6. I take a positive attitude toward myself.')
input_question (positive, negative, total)

positive = print('7. On the whole, I am satisfied with myself.')
input_question (positive, negative, total)

negative = print('8. I wish I could have more respect for myself.')
input_question (positive, negative, total)

negative = print('9. I certainly feel useless at times.')
input_question (positive, negative, total)

negative = print('10. At times I think I am no good at all.')
input_question (positive, negative, total)




print(f'Your score is {total}.')

print('A score below 15 may indicate problematic low self-esteem.')
