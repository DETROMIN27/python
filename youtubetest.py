from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout,QVBoxLayout,QRadioButton,QMessageBox,QLabel
from PyQt5.QtCore import Qt

WINSIZE = (600,450)
TITLE = "TEST"
QW = "Як звали першого ютуб-блогера, який набрав 100000000 підписників?"
ANSW = ["PewDiePie","Рет і Лінк,","SlivkiShow","TheBrianMaps","Mister Max","EeOneGuy"]

app = QApplication([])
win = QWidget()
win.resize(WINSIZE[0],WINSIZE[1])
win.setWindowTitle(TITLE)
win.move(600,200)

qw = QLabel(QW)
rbn_list = list()
for i in range(6):
    lbl = QRadioButton(ANSW[i])
    rbn_list.append(lbl)

lineh1 = QHBoxLayout()
lineh2 = QHBoxLayout()
lineh3 = QHBoxLayout()
lineh4 = QHBoxLayout()
lineh5 = QHBoxLayout()
lineh6 = QHBoxLayout()
main_line = QVBoxLayout()

lineh1.addWidget(qw,alignment=Qt.AlignCenter)
lineh2.addWidget(rbn_list[0],alignment=Qt.AlignCenter)
lineh2.addWidget(rbn_list[1],alignment=Qt.AlignCenter)
lineh3.addWidget(rbn_list[2],alignment=Qt.AlignCenter)
lineh3.addWidget(rbn_list[3],alignment=Qt.AlignCenter)
lineh4.addWidget(rbn_list[4],alignment=Qt.AlignCenter)
lineh4.addWidget(rbn_list[5],alignment=Qt.AlignCenter)


main_line.addLayout(lineh1)
main_line.addLayout(lineh2)
main_line.addLayout(lineh3)
main_line.addLayout(lineh4)
main_line.addLayout(lineh5)
main_line.addLayout(lineh6)

def win_show():
    mess = QMessageBox()
    mess.setWindowTitle("win!")
    mess.setText("YOU WIN!")
    mess.show()
    mess.exec()

def lose_show():
    mess = QMessageBox()
    mess.setWindowTitle("lose")
    mess.setText("YOU LOSE!")
    mess.show()
    mess.exec()


rbn_list[0].clicked.connect(win_show)
rbn_list[2].clicked.connect(lose_show)
rbn_list[1].clicked.connect(lose_show)
rbn_list[3].clicked.connect(lose_show)
rbn_list[4].clicked.connect(lose_show)
rbn_list[5].clicked.connect(lose_show)




win.setLayout(main_line)
win.show()
app.exec()


