from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import json
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])
def create_note():
    note_name, result = QInputDialog.getText(main_win, "Добавить заметку", "Название заметки:")
    if result == True:
        list_notes.addItem(note_name)
        notes[note_name] = {'текст': '', 'теги': []}
def save_notes():
    name = list_notes.selectedItems()[0].text()
    notes[name]['текст'] = field_text.toPlainText()
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)
def del_notes():
    name = list_notes.selectedItems()[0].text()
    del notes[name]
    list_notes.clear()
    list_notes.addItems(notes)
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)
def add_tag():
    name = list_notes.selectedItems()[0].text()
    tag = field_tag.text()
    if tag in notes[name]['теги']:
        nope = QMessageBox()
        nope.setText('Данный тег в выбранной заметке существует.')
        nope.exec_()
    else:
        notes[name]['теги'].append(tag)
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        show_note()
def del_tag():
    name = list_notes.selectedItems()[0].text()
    tag = list_tags.selectedItems()[0].text()
    notes[name]['теги'].remove(tag)
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    show_note()
def search_tag():
    search_notes.clear()
    tag = field_tag.text()
    for note in notes:
        if tag in notes[note]['теги']:
            search_notes.append(note)
    list_notes.clear()
    list_notes.addItems(search_notes)


app = QApplication([])
app.setStyle('Fusion')
main_win = QWidget()
main_win.resize(900, 600)
main_win.setWindowTitle('Заметки')
#виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')
 
button_note_create = QPushButton('Создать заметку') #появляется окно с полем "Введите имя заметки"
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')
 
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_add = QPushButton('Добавить к заметке')
button_del = QPushButton('Открепить от заметки')
button_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')
 


#расположение виджетов по лэйаутам
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
 
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
 
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)
 
col_2.addLayout(row_3)
col_2.addLayout(row_4)
 
layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
main_win.setLayout(layout_notes)
#
btn_del = QPushButton('Удалить')

search_notes = []


notes = {
            'Заметка':
                {
                    'текст': 'Очень важная заметка',
                    'теги': ['тег 1', 'тег 2']
                }
        }

#with open('notes.json', 'w', encoding='utf-8') as file:
#    json.dump(notes, file, sort_keys=True, ensure_ascii=False)

notes = []
    
with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)

list_notes.addItems(notes)


list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(create_note)
button_note_save.clicked.connect(save_notes)
button_note_del.clicked.connect(del_notes)
button_add.clicked.connect(add_tag)
button_del.clicked.connect(del_tag)
button_search.clicked.connect(search_tag)
main_win.show()
app.exec_()