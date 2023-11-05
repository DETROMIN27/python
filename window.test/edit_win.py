from PyQt5.QtWidgets import (QWidget,QLabel,QPushButton,QLineEdit,QGridLayout)
 
edit_win = QWidget()
edit_win.resize(600,500)
edit_win.move(300,300)

lbl_qw_edit = QLabel("Qw qw")
lbl_ans_edit = QLabel("Right answ text")
lbl_wr1_edit = QLabel("Wrong answer 1")
lbl_awr2_edit = QLabel("Wrong answer 2")
lbl_wr3_edit = QLabel("Wrong answer 3")

edit_qw = QLineEdit()
edit_ans = QLineEdit()
edit_wrong1 = QLineEdit()
edit_wrong2 = QLineEdit()
edit_wrong3 = QLineEdit()

btn_add = QPushButton("Add Question")
btn_clear = QPushButton("Clear")

lbl_stat = QLabel("Statistic")
lbl_count = QLabel("Count of answer")
lbl_count_right = QLabel("Count of right answer")
lbl_good = QLabel("Good %")

btn_back = QPushButton("back")

grid = QGridLayout()
grid.addWidget(lbl_qw_edit,0,0)
grid.addWidget(edit_qw,0,1)

grid.addWidget(lbl_ans_edit,1,0)
grid.addWidget(edit_ans,1,1)

grid.addWidget(lbl_wr1_edit,2,0)
grid.addWidget(edit_wrong1,2,1)

grid.addWidget(lbl_awr2_edit,3,0)
grid.addWidget(edit_wrong2,3,1)

grid.addWidget(lbl_wr3_edit,4,0)
grid.addWidget(edit_wrong3,4,1)

grid.addWidget(btn_add,5,0)
grid.addWidget(btn_clear,5,1)

grid.addWidget(lbl_stat,6,0,2,0)
grid.addWidget(lbl_count,7,0,2,0)
grid.addWidget(lbl_count_right,8,0,2,0)
grid.addWidget(lbl_good,9,0,2,0)

grid.addWidget(btn_back,10,0,2,0)

edit_win.setLayout(grid)
edit_win.hide()


