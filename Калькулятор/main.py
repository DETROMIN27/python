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
        def work(self,btn):
            if btn.text()=="=":
                ...

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()