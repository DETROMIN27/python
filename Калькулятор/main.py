from PyQt5.QtWidgets import QApplication,QMainWindow,QButtonGroup,QWidget,QLabel
from calculator import Ui_MainWindow

class Widget (QMainWindow):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.num1 = ""
        self.num2 = ""
        self.operation = ""
        all_bnt = self.ui.centralwidget.findChildren(QWidget)
        self.group = QButtonGroup()
        for btn in all_bnt: 
            if type(btn)!=QLabel:
                self.group.addButton(btn)
        self.group.buttonClicked.connect(self.work)
    def work (self,btn):
        if btn.text()=="=":  
            if self.operation == "-":
                res = int (self.num1) - int(self.num2)
                txt = self.ui.label.text()
                self.ui.label.setText(txt+"="+str(res))
            elif self.operation == "+":
                res = int(self.num1) + int(self.num2)
                txt = self.ui.label.text()
                self.ui.label.setText(txt+"="+str(res))
            elif self.operation == "*":
                res = int(self.num1) * int(self.num2)
                txt = self.ui.label.text()
                self.ui.label.setText(txt+"="+str(res))
            elif self.operation == "/":
                if self.num2 != 0 :
                    res = int(self.num1) / int(self.num2)
                    txt = self.ui.lbl_win.text()
                    self.ui.label.setText(txt+" = "+str(res))
                else:
                    self.ui.label.setText("Error")
                    res=""
                self.num = str(res)
                self.num2 = ""
                self.operation=""
            elif btn.text in ["-","+","*","/"]:
                self.operation = btn.text()
                txt = self.ui.label.text()
                self.ui.label.setText(txt+" "+self.operation+" ")
            elif btn.text=="CE":
                self.num1=""
                self.num2=""
                self.operation=""
                self.ui.label.setText("0")
            else:
                if self.ui.label.text()=="0":
                    txt = ""
                else:
                    self.ui.label.text()
                num = btn.text()
                if self.operation=="":
                    self.num1+=num
                else:
                    self.num2+=num
                txt+=num
                self.ui.label.setText(txt)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()