# QUIZ GAME

import random

questions = [
    {'Que.': ' What is the pH value of the human body?', 'options': ['9.2 to 9.8', '7.0 to 7.8', '6.1 to 6.3', '5.4 to 5.6'], 'correct_op_index': 2},
    {'Que.': ' Elections to panchayats in state are regulated by _____', 'options': ['Gram panchayat', 'Nagar Nigam', 'Election Commission of India', 'State Election Commission'], 'correct_op_index': 3},
    {'Que.': ' Pustaz grasslands are situated at ____', 'options': ['South Africa', 'China', 'Hungary', 'USA'], 'correct_op_index': 2},
    {'Que.': ' Right to emergency medical aid is a ____', 'options': ['Legal Right', 'Illegal Right', 'Constitutional Right', 'Fundamental Right'], 'correct_op_index': 3},
    {'Que.': 'When the metal reacts with dilute acid, which gas is formed?', 'options': ['Carbon Dioxide', 'Helium', 'Neon', 'Hydrogen'], 'correct_op_index': 3},
    {'Que.': 'Which of the following is responsible for nitrogen fixation?', 'options': ['Fungus', 'Bacteria', 'Virus', 'Insects'], 'correct_op_index': 1},
    {'Que.': 'Where is Lomus Rishi Cave located?', 'options': ['Nasik', 'Gaya', 'Varanasi', 'Bhubaneswar'], 'correct_op_index': 1},
    {'Que.': 'Which of the following is a scalar quantity?', 'options': ['Force', 'Pressure', 'Momentum', 'Acceleration'], 'correct_op_index': 2},
    {'Que.': 'Salt is obtained from sea water through which process?', 'options': ['Adsorption', 'Evaporation', 'Sublimation', 'Absorption'], 'correct_op_index': 1},
    {'Que.': 'Which of the given industries uses limestone as a raw material?', 'options': ['Paper', 'Cement', 'Textile', 'Leather'], 'correct_op_index': 1},
]

def start_quiz(questions):
    score = 0

    for question in questions:
        print(question['Que.'])
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")

        while True:
            try:
                user_input = int(input('Enter the number of your option - ')) - 1
                if 0 <= user_input < len(question['options']):
                    break
                else:
                    print("Invalid input. Please enter a valid option number.")
            except ValueError:
                print('Invalid input. Please enter a valid option number.')

        correct_index = question['correct_op_index']

        if user_input == correct_index:
            print('You Got 1 Point !!')
            score += 1
        else:
            print(f"Wrong. The Correct Answer is : {question['options'][correct_index]}\n")
    print(f'You Completed the Quiz! Your score : {score}/{len(questions)}')
start_quiz(questions)



