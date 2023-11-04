from PyQt5.QtWidgets import (QWidget,QLabel,QPushButton,QLineEdit,QGridLayout)
 
edit_win = QLabel()

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