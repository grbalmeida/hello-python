class LogMixin: # Mixin adds functionality to other classes
  @staticmethod
  def write(message):
    with open('object-oriented-programming/multiple-inheritance/log.log', 'a+') as file:
      file.write(message)
      file.write('\n')

  def log_info(self, message):
    self.write(f'INFO: {message}')

  def log_error(self, message):
    self.write(f'ERROR: {message}')
