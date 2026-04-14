import sys
from PySide6.QtWidgets import (
    QApplication, 
    QGridLayout, 
    QHBoxLayout, 
    QLineEdit, 
    QPushButton, 
    QWidget,
    QSizePolicy, 
    )

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draft of Calculator Layout")

        # Define Layout
        input_label = QHBoxLayout()
        layout = QGridLayout()
        line_edit = QLineEdit(placeholderText= "Enter Here.")
        calculator_layout = [
            ["", "", "", ""],
            ["", "", "DEL", "AC"],
            ["1", "2", "3", "*"],
            ["4", "5", "6", "/"],
            ["7", "8", "9", "="],
            ["0", "-", "+", ""]
            
        ]

        input_label.addWidget(line_edit)

        # use for loops to create the layout
        for row, row_data in enumerate(calculator_layout):
            for column, text in enumerate(row_data):
                if text:
                    btn = QPushButton(text)
                    if text == "=":
                        btn.setFixedSize(30, 65)
                        layout.addWidget(btn, row, column, 2, 1)
                    else:
                        btn.setFixedSize(30, 30)
                        layout.addWidget(btn, row, column)

        # Add to the main window
        layout.addLayout(input_label, 0,0 ,1, 4)
        self.setLayout(layout)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
