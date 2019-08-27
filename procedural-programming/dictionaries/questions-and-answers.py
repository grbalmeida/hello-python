questions = {
  'First Question': {
    'question': 'How much is 2 + 2?',
    'answers': { 'a': '1', 'b': '4', 'c': '5' },
    'correct_answer': 'b'
  },
  'Second question': {
    'question': 'How much is 3 * 2?',
    'answers': { 'a': '4', 'b': '10', 'c': '6' },
    'correct_answer': 'c'
  }
}

correct_answers = 0

for question_key, question_value in questions.items():
  print(f'{question_key}: {question_value.get("question")}')

  print('\tAnswers: ')

  for response_key, response_value in question_value.get('answers').items():
    print(f'\t{response_key}: {response_value}')

  user_response = input('Your response: ')

  if user_response == question_value['correct_answer']:
    correct_answers += 1
    print('You got the answer right')
  else:
    print('You got the answer wrong')

amount_of_questions = len(questions)
percentage_correct_answers = correct_answers / amount_of_questions * 100

print(f'You got {correct_answers} questions right')
print(f'Your hit percentage was {percentage_correct_answers}%')
