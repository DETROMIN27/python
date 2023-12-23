from PyQt5.QtCore import Qt  #імопртуємо Qt
from notes import Ui_Notes  # імпоруємо Ui_Notes  з notes
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox #імпортуємо віджети
from data import write_json, read_json # імпортуємо  write_json,resd_json
 
 
class MainWindow(QMainWindow): # клас  MainWindow
    def __init__(self): #
        super().__init__() 
        self.ui = Ui_Notes() 
        self.ui.setupUi(self) 
        self.name_file = "notes.json" 
        self.notes = read_json(self.name_file) 
        name_note = list(self.notes.keys()) 
        self.ui.note_list1.addItems(name_note) 
        name_note = name_note[0] 
        self.set_note(name_note) 
        self.connects()  
 
    def set_note(self, name_note): # задати нотатку
        note = self.notes[name_note] 
        self.ui.txt_edit.clear() 
        self.ui.txt_edit.setText(note["text"]) 
        self.ui.note_list2.clear()  
        self.ui.note_list2.addItems(note["teg"]) 
        item = self.ui.note_list1.findItems(name_note, Qt.MatchExactly) 
        n = self.ui.note_list1.row(item[0]) 
        item = self.ui.note_list1.findItems(name_note, Qt.MatchExactly) 
        n = self.ui.note_list1.row(item[0]) 
        self.ui.note_list1.setCurrentRow(n)
    
    def add_note(self): # додати нотатку
        name_note, do = QInputDialog.getText(self, 
                                            "notes_edit", 
                                            "Введіть назву нової замітки") 
        self.notes[name_note] = {"text": "", "teg": []} 
        write_json(self.notes, self.name_file) 
        self.ui.note_list1.addItem(name_note) 
        self.set_note(name_note) 

    def add_teg(self): # додати тег
        name_teg, do = QInputDialog.getText(self, 
                                            "notes_edit", 
                                            "Введіть назву нового тега") 
        name_note = self.ui.note_list1.currentItem().text()
        self.notes[name_note]["teg"].append(name_teg)
        write_json(self.notes, self.name_file)
        self.ui.note_list2.addItem(name_teg)

    
    def del_teg(self): # видалити тег
        iter = self.ui.text_list.cuurentItem()
        name_teg = item.text()
        item = self.ui.note
        name_note = item.text()
        self.notes[name_note]["teg"].remove(name_teg)
        write_json(self.notes, self.name_file)
        num = self.ui.note_list1.row(item)
        self.ui.name_list1.takeItem(num)

 
    def delete_note(self): # видалити нотатку 
        iter = self.ui.note_list1.currentItem() 
        name = iter.text()
        del self.notes[name]
        num =  self.ui.note_list1.row(iter)
        write_json(self.notes,self.name_file) 
        self.ui.note_list1.takeItem(num)
     
    def save_note (self): # зберегти нотатку
        iter = self.ui.note_list1.currentItem() 
        name = iter.text()
        text = self.ui.txt_edit.toPlainText()
        self.notes[name]["text"] = text
        write_json(self.notes,self.name_file)
        mes = QMessageBox(self.ui.main_win)
        mes.setText("Замітку збережено")
        mes.show()
        mes.exec()

    def find_teg (self): # знайти тег
        text = self.ui.teg_find.text()
        teg_notes = dict()
        for name_note in self.notes:
            if text in self.notes[name_note]["teg"]:
                teg_notes[name_note] = self.notes[name_note]
        self.ui.note_list1.clear()
        names = list(teg_notes.keys())
        self.ui.note_list1.addItems(names)
        self.set_note(names[0])

    def reset (self): #заново
        self.ui.note_list1.clear()
        name_note = list(self.notes.keys()) 
        self.ui.note_list1.addItems(name_note) 
        name_note = name_note[0] 
        self.set_note(name_note) 


    def connects(self): #зєднання кнопок з їх функією
        self.ui.btn_add_note.clicked.connect(self.add_note)
        self.ui.btn_del_note.clicked.connect(self.delete_note)
        self.ui.btn_save_note.clicked.connect(self.save_note)
        self.ui.btn_add_teg.clicked.connect(self.add_teg)
        self.ui.note_list1.itemClicked.connect(self.clicked_note)
        self.ui.btn_final.clicked.connect(self.find_teg)
        #self.ui.note_list1.currentItemChanged.connect(self.clicked_note)
        self.ui.btn_reset.clicked.connect(self.reset)

    def clicked_note (self): #нажати на нотатку 
        iter = self.ui.note_list1.currentItem()
        name_note = iter.text()
        self.set_note(name_note)

 
app = QApplication([]) 
win = MainWindow()
win.show() 
app.exec()