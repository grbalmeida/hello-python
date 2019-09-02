from writer import Writer
from pen import Pen
from typewriter import Typewriter

writer = Writer('John')
pen = Pen('Bic')
typewriter = Typewriter()

print(writer.name)
print(pen.brand)
print(typewriter)

writer.tool = pen
writer.tool.write()

writer.tool = typewriter
writer.tool.write()

del writer

print(pen.brand)
pen.write()
typewriter.write()
