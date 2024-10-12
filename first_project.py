from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
win = QWidget()
winner = QLabel("Натисніть на кнопку, щоб отримати переможця")
number = QLabel("?")
button = QPushButton("Згенерувати")

app.setStyleSheet("""  
            QWidget {background-color: rgb(220,240,200)}
            QLabel {font-size:20px}
            QPushButton {font-size: 12px; background-color: rgb(10,200,150)}
                """)

win.resize(500, 500)
win.setWindowTitle("My First Application")

v_line = QVBoxLayout()
v_line.addWidget(winner, alignment = Qt.AlignCenter)
v_line.addWidget(number, alignment = Qt.AlignCenter)
v_line.addWidget(button, alignment = Qt.AlignCenter)
win.setLayout(v_line)

def show_winner():
    number.setText(str(randint(1,100)))
    winner.setText("Переможець:")

button.clicked.connect(show_winner)

win.show()
app.exec_()
