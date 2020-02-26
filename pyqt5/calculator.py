import sys
from PyQt5.QtWidgets import (
  QMainWindow,
  QApplication,
  QWidget,
  QGridLayout,
  QPushButton,
  QLineEdit,
  QSizePolicy
)

class Calculator(QMainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle('Calculator')
    self.setFixedSize(400, 400)
    self.cw = QWidget()
    self.grid = QGridLayout(self.cw)
    self.display = QLineEdit()
    self.grid.addWidget(self.display, 0, 0, 1, 5) # First line, first column, 1 line, 5 columns
    self.display.setDisabled(True)
    self.setStyleSheet(
      '* {background: #FFF; color: #000; font-size: 30px;}'        
    )
    self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    self.add_button(QPushButton('7'), 1, 0, 1, 1)
    self.add_button(QPushButton('8'), 1, 1, 1, 1)
    self.add_button(QPushButton('9'), 1, 2, 1, 1)
    self.add_button(QPushButton('+'), 1, 3, 1, 1)
    self.add_button(
      QPushButton('C'), 1, 4, 1, 1,
      function=lambda: self.display.setText(''),
      style='background: #D5580D; color: #FFF; font-weight: 700;'
    )

    self.add_button(QPushButton('4'), 2, 0, 1, 1)
    self.add_button(QPushButton('5'), 2, 1, 1, 1)
    self.add_button(QPushButton('6'), 2, 2, 1, 1)
    self.add_button(QPushButton('-'), 2, 3, 1, 1)
    self.add_button(
      QPushButton('<-'), 2, 4, 1, 1,
      function=lambda: self.display.setText(
        self.display.text()[:-1]    
      ),
      style='background: #13823A; color: #FFF; font-weight: 700;'
    )

    self.add_button(QPushButton('1'), 3, 0, 1, 1)
    self.add_button(QPushButton('2'), 3, 1, 1, 1)
    self.add_button(QPushButton('3'), 3, 2, 1, 1)
    self.add_button(QPushButton('/'), 3, 3, 1, 1)
    self.add_button(QPushButton(''), 3, 4, 1, 1)

    self.add_button(QPushButton('.'), 4, 0, 1, 1)
    self.add_button(QPushButton('0'), 4, 1, 1, 1)
    self.add_button(QPushButton(''), 4, 2, 1, 1)
    self.add_button(QPushButton('*'), 4, 3, 1, 1)
    self.add_button(
      QPushButton('='), 4, 4, 1, 1,
      function=self.eval,
      style='background: #095177; color: #FFF; font-weight: 700;'
    )

    self.setCentralWidget(self.cw)

  def add_button(self, button, row, column, rowspan, colspan, function=None, style=None):
    self.grid.addWidget(button, row, column, rowspan, colspan)
    
    if not function:
      button.clicked.connect(
        lambda: self.display.setText(
          self.display.text() + button.text()    
        )        
      )
    else:
      button.clicked.connect(function)

    if style:
      button.setStyleSheet(style)

  def eval(self):
    try:
      self.display.setText(
        str(eval(self.display.text()))        
      )
    except Exception as e:
      self.display.setText('Invalid result')

if __name__ == '__main__':
  qt = QApplication(sys.argv)
  calculator = Calculator()
  calculator.show()
  qt.exec_()
