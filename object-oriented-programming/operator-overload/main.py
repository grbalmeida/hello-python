class Rectangle:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def get_area(self):
    return self.x * self.y

  def __repr__(self):
    return f'<class \'Rectangle({self.x}, {self.y})\'>'

  def __add__(self, other):
    new_x = self.x + other.x
    new_y = self.y + other.y
    return Rectangle(new_x, new_y)

  def __lt__(self, other):
    self_area = self.get_area()
    other_area = other.get_area()

    return self_area < other_area

  def __gt__(self, other):
    self_area = self.get_area()
    other_area = other.get_area()

    return self_area > other_area

  def __eq__(self, other):
    self_area = self.get_area()
    other_area = other.get_area()

    return self_area == other_area


first_rectangle = Rectangle(10, 23)
second_rectange = Rectangle(4, 14)

print(first_rectangle + second_rectange)
print(first_rectangle < second_rectange)
print(first_rectangle > second_rectange)
print(Rectangle(10, 10) == Rectangle(5, 5))
print(Rectangle(10, 10) == Rectangle(10, 10))
