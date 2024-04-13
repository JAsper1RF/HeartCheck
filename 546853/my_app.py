
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import test_description

app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Тест Руфье')

start_button = QPushButton('Начать')

start_button.text()

text = QLabel('Тест руфье')

text_main = QLabel(test_description)

v_line = QVBoxLayout()
v_line.addWidget(text, alignment = Qt.AlignCenter)
v_line.addWidget(text_main, alignment = Qt.AlignCenter)
v_line.addWidget(start_button, alignment = Qt.AlignCenter)

main_win.setLayout(v_line)
app.exec_()