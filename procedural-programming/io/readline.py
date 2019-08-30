from FILE import FILE

file = open(FILE, 'r')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
file.close()
