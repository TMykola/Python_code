from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QVBoxLayout,QRadioButton,QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
app = QApplication([])
win = QWidget()
que = QLabel('В якому році канал отримав "золоту кнопку" від YouTube?')
v_line = QVBoxLayout()
h_line = QHBoxLayout()
h_line2 = QHBoxLayout()

win.setWindowTitle("Конкурс від Crazy People")
win.resize(400,300)

win.setLayout(v_line)
v_line.addWidget(que, alignment = Qt.AlignCenter)
v_line.addLayout(h_line2)
v_line.addLayout(h_line)

answer1 = QRadioButton("2005")
answer2 = QRadioButton("2010")
answer3 = QRadioButton("2015")
answer4 = QRadioButton("2020")

h_line.addWidget(answer1, alignment= Qt.AlignCenter)
h_line.addWidget(answer2, alignment= Qt.AlignCenter)
h_line2.addWidget(answer3, alignment= Qt.AlignCenter)
h_line2.addWidget(answer4, alignment= Qt.AlignCenter)

def winn():
    wictory_win = QMessageBox()
    wictory_win.setText("You win")
    wictory_win.exec_()
def lose():
    lose_lose = QMessageBox()
    lose_lose.setText("You lose")
    lose_lose.exec_()

answer1.clicked.connect(lose)
answer2.clicked.connect(lose)
answer3.clicked.connect(winn)
answer4.clicked.connect(lose)


win.show()
app.exec_()
