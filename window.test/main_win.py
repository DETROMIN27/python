from PyQt5.QtWidgets import (QWidget,QLabel,QHBoxLayout,QVBoxLayout,
                             QPushButton,QRadioButton,QSpinBox,QGroupBox,QButtonGroup,
                             )
from PyQt5.QtCore import Qt

#налаштування вікна
test_win = QWidget()
test_win.resize(600,500)
test_win.setWindowTitle("Memory Card")

#додавання кнопок
btn_menu = QPushButton("Menu")
btn_rest = QPushButton("Time")
time_rest = QSpinBox()
time_rest.setValue(30)
lbl_rest = QLabel("minutes")

#запитання
lbl_qw = QLabel("Question")

#відповідь
box_ans = QGroupBox()
box_ans.setTitle("Answers")

#4 відповіді
rbn_list = list()
rbn_group = QButtonGroup()
for i in range (4):
    rbt = QRadioButton("a")
    rbn_group.addButton(rbt)
    rbn_list.append(rbt)

#кнопки
box_result = QGroupBox()
box_result.setTitle("Result")
lbl_ans = QLabel("ans")
lbl_result = QLabel("result")

#перевірка відповіді
btn_check = QPushButton("Check")

#вертикальні та горизонтальні лінії
main_line = QVBoxLayout()
lineh1 = QHBoxLayout()
lineh2 = QHBoxLayout()
lineh3 = QHBoxLayout()
lineh4 = QHBoxLayout()

#прикріплюєм віджети на лінії
lineh1.addWidget(btn_menu)
lineh1.addStretch(3)
lineh1.addWidget(btn_rest)
lineh1.addWidget(time_rest)
lineh1.addWidget(lbl_rest)

lineh2.addWidget(lbl_qw,alignment=Qt.AlignCenter)
lineh3.addWidget(box_result)
box_result.hide()
lineh3.addWidget(box_ans)

lineh4.addStretch(2)
lineh4.addWidget(btn_check)
lineh4.addStretch(2)

line_v1 = QVBoxLayout()
line_v1.addWidget(lbl_result,alignment=Qt.AlignLeft)
line_v1.addWidget(lbl_ans, alignment=Qt.AlignCenter)
box_result.setLayout(line_v1)

line_v2 = QVBoxLayout()
line_v3 = QVBoxLayout()
lineh5 = QHBoxLayout()

line_v2.addWidget(rbn_list[0])
line_v2.addWidget(rbn_list[1])
line_v3.addWidget(rbn_list[2])
line_v3.addWidget(rbn_list[3])
lineh5.addLayout(line_v2)
lineh5.addLayout(line_v3)
box_ans.setLayout(lineh5)




main_line.addLayout(lineh1)
main_line.addLayout(lineh2)
main_line.addLayout(lineh3)
main_line.addLayout(lineh4)

test_win.setLayout(main_line)








