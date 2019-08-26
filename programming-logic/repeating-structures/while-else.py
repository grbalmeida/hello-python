counter = 1
accumulator = 1

while counter <= 10:
  print(counter, accumulator)

  if counter > 5:
    break

  accumulator += counter
  counter += 1
else:
  print('This will not be executed')

print('This will be executed')

