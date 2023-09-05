import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit


class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('ToDO List')
        self.setGeometry(100, 100, 400, 400)

        self.task_list = QListWidget()

        self.task_input = QLineEdit()
        self.add_button = QPushButton('Add Task')
        self.remove_button = QPushButton('Remove Task')
        ##CSS

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)

        layout = QVBoxLayout()
        task_layout = QHBoxLayout()
        task_layout.addWidget(self.task_input)
        task_layout.addWidget(self.add_button)
        layout.addLayout(task_layout)
        layout.addWidget(self.task_list)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()

    def remove_task(self):

        selected_item = self.task_list.currentItem()
        if selected_item:
            self.task_list.takeItem(self.task_list.row(selected_item))



def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())
    window = ToDoListApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
