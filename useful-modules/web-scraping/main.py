import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for question in html.select('.question-summary'):
  title = question.select_one('.question-hyperlink')
  date = question.select_one('.relativetime')
  votes = question.select_one('.vote-count-post strong')

  print(f'Question: {title.text}')
  print(f'Votes: {votes.text}')
  print(f'Date: {date.text}')
  print()
