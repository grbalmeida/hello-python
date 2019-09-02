from electronic import Electronic
from log import LogMixin

class Smartphone(Electronic, LogMixin):
  def __init__(self, name):
    super().__init__(name)
    self._connected = False

  def connect(self):
    if not self._on:
      info = f'{self._name} not connected'
      print(info)
      self.log_info(info)
      return

    if self._connected:
      error = f'{self._name} already connected'
      print(error)
      self.log_error(error)
      return

    info = f'{self._name} is connected'
    print(info)
    self.log_info(info)
    self._connected = True

  def disconnect(self):
    if not self._connected:
      error = f'{self._name} not connected'
      print(error)
      self.log_error(error)
      return

    info = f'{self._name} is disconnected'
    print(info)
    self.log_info(info)
    self._connected = False
