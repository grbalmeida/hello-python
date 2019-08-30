from FILE import FILE

file = open(FILE, 'w+')
file.write('First line\n')
file.write('Second line\n')
file.write('Third line')
file.close()
