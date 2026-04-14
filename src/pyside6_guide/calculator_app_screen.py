import sys
from PySide6.QtWidgets import (
    QApplication, 
    QVBoxLayout, 
    QHBoxLayout,
    QGridLayout, 
    QLineEdit, 
    QPushButton, 
    QWidget,
    QSizePolicy, 
    )
from PySide6.QtCore import Qt


class CalculatorAppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator App Screen")

        input_label = QHBoxLayout()
        layout = QGridLayout()
        self.line_edit = QLineEdit()
        calculator_layout = [
            ["", "", "", ""],
            ["ANS", "", "DEL", "AC"],
            ["1", "2", "3", "*"],
            ["4", "5", "6", "/"],
            ["7", "8", "9", "="],
            ["0", "-", "+", ""]
        ]

        input_label.addWidget(self.line_edit)

        # use for loops to create the layout
        for row, row_data in enumerate(calculator_layout):
            for column, text in enumerate(row_data):

                # Is it a button or space?
                if text:
                    buttons = QPushButton(text)

                    # Is it a equal and ANS button?
                    # if it is, adjust the size of it  
                    if text == "ANS":
                        buttons.setFixedSize(65, 25)
                        layout.addWidget(buttons, row, column, 1, 2)
                    elif text == "=":
                        buttons.setFixedSize(30, 65)
                        layout.addWidget(buttons, row, column, 2, 1)
                    else:
                        buttons.setFixedSize(30, 30)
                        layout.addWidget(buttons, row, column)

                    # Is it a DEL, AC or equal button?
                    # if it is, add special function to them
                    if text == "=":
                        buttons.clicked.connect(lambda: self.process_input())
                    elif text == "ANS":
                        buttons.clicked.connect(lambda: self.get_the_previous_answer())
                    elif text == "AC":
                        buttons.clicked.connect(lambda: self.clear())
                    elif text == "DEL":
                        buttons.clicked.connect(lambda: self.delete())  
                    else:
                        buttons.clicked.connect(lambda _, x=str(text): self.add_number(x))  

        # adding layout to main window
        layout.addLayout(input_label, 0,0 ,1, 4)
        self.setLayout(layout)

    def add_number(self, num):
        """Enter the number corresponding to the pressed button"""
        current_text = self.line_edit.text()
        self.line_edit.setAlignment(Qt.AlignLeft)
        self.line_edit.setText(current_text + num)
    
    def process_input(self):
        """process the input and print the output"""
        self.line_edit.setAlignment(Qt.AlignRight)
        try:
            self.answer = round(eval(self.line_edit.text()), 2)
            self.line_edit.setText(str(self.answer))
        except NameError and SyntaxError:
            self.output_label.setText("ERROR!!!")
    
    def get_the_previous_answer(self):
        """recall the previous output"""
        try:
            self.line_edit.setAlignment(Qt.AlignLeft)
            self.line_edit.setText(str(self.answer))
        except AttributeError:
            self.output_label.setText("ERROR!!!")

    def clear(self):
        """Clear the text in the line edit"""
        self.line_edit.clear()
    
    def delete(self):
        """delete one letter each time it is pressed"""
        current_text = self.line_edit.text()
        new_text = current_text[:-1]
        self.line_edit.setText(new_text)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorAppWindow()
    window.show()
    sys.exit(app.exec())
