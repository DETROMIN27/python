from PyQt5.QtWidgets import QApplication,QMessageBox
app = QApplication([])
from main_win import*
from data import qw_list
from random import shuffle, choice

choice_ans = ""
qw = ""


def new_qw ():
    global qw
    qw_text = lbl_qw.text()
    qw = choice(qw_list)
    while qw_text == qw.qw:
        qw = choice(qw_list)
    answers = [qw.ans,qw.wrong1,qw.wrong2,qw.wrong3]
    shuffle(answers)
    lbl_qw.setText(qw.qw)
    for i in range(4):
        rbn_list[i].setText(answers[i])
def nul_ans():
    global choice_ans
    choice_ans =""
    rbn_group.setExclusive(False)
    for i in range (4):
        rbn_list[i].setChecked(False)
    rbn_group.setExclusive(True)
def check_ans():
    if btn_check.text()=="Check":
        if choice_ans == "":
            mess = QMessageBox()
            mess.setText("Text")
            mess.show()
            mess.exec()
        else:

            if choice_ans == qw.ans:
                lbl_result.setText("Чудово!")
                qw.right_ans()
            else: 
                lbl_result.setText("Не вірно!")
                qw.wrong_ans()
            lbl_ans.setText(qw.ans)
            btn_check.setText("Next")
            box_ans.hide()
            box_result.show()
    else:
        new_qw()
        nul_ans()
        btn_check.setText("Check")
        box_ans.show()
        box_result.hide()
        
                    
def click_ans(rbn):
    global choice_ans
    choice_ans = rbn.text()


new_qw()
rbn_group.buttonClicked.connect(click_ans)
btn_check.clicked.connect(check_ans)

test_win.show()
app.exec()