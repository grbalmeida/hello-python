from time import sleep

books = list()

books.append('First book')
books.append('Second book')
books.append('Third book')
books.append('Fourth book')
books.append('Fifth book')

for i in range(5):
  book_removed = books.pop()
  print(books, book_removed)
  sleep(1)
