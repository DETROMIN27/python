from notes import Ui_Notes
from PyQt5.QtWidgets import QApplication, QMainWindow,QInputDialog 
from data import write_json,read_json


class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.ui = Ui_Notes()
        self.ui.setupUi(self) 
        self.name_fail = "notes.json"
        self.notes = read_json(self.name_fail)
        name_note = list(self.notes.keys())
        self.ui.note_list1.addItems(name_note)
        name_note = name_note[0]
        self.set_note(name_note)
        self.connects()

    def set_note(self,name_note):
        note = self.notes[name_note]
        self.ui.txt_edit.clear()
        self.ui.txt_edit.setText(note["text"])
        self.ui.note_list2.clear()
        self.ui.note_list2.addItems(note["teg"])
        self.ui.note_list1.setCurrentRow()

    def add_note(self):
        name_note,do=QInputDialog.getText(self,
                                          "notes_edit",
                                          "Введіть назву нової замітки")
        self.notes[name_note]={"text":"","teg":[]}
        write_json(self.notes,self.name_fail)
        self.set_note(name_note)        
        
        
    def connects(self):
        self.ui.btn_add_note.clicked.connect(self.add_note)

 
app = QApplication([]) 
win = MainWindow()
win.show() 
app.exec()