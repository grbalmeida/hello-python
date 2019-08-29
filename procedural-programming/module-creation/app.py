from double_list_values import double_list_value
from multiply import multiply
from pi import PI
from other import say_hi

if __name__ == '__main__':
  my_list = list(range(1, 6))

  print(double_list_value(my_list))
  print(multiply(my_list))
  print(f'{PI:.4f}')
  say_hi()
