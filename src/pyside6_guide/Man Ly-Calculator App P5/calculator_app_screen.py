import sys
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QGridLayout, 
    QLineEdit, 
    QPushButton, 
    QWidget, 
    )
from PySide6.QtCore import Qt

class CalculatorAppWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Calculator App Screen")
        self.parent = parent

        # Set intial values of size
        self.error_message = "ERROR!!!"
        default_size = 40
        width_equal_button = default_size
        height_equal_button = (width_equal_button * 2) +5
        width_ans_button = (default_size *2) +  5
        height_ans_button = default_size
        
        # Define the layouts
        input_label = QHBoxLayout()
        layout = QGridLayout()
        self.line_edit = QLineEdit()
        calculator_layout = [
            ["", "", "", ""],
            ["ANS", "", "DEL", "AC"],
            ["1", "2", "3", "*"],
            ["4", "5", "6", "/"],
            ["7", "8", "9", "="],
            ["0", "-", "+", ""],
            ["", "Back", "", ""]
        ]
        
        # Create the calculator layout by using for loops
        input_label.addWidget(self.line_edit)
        for row, row_data in enumerate(calculator_layout):
            for column, text in enumerate(row_data):

                # Is it a button or space?
                if text:
                    buttons = QPushButton(text)

                    # Is it a equal, ANS, and back button?
                    # if it is, adjust the size of it  
                    if text == "ANS":
                        buttons.setFixedSize(width_ans_button,
                                            height_ans_button)
                        layout.addWidget(buttons, row, column, 1, 2)
                    elif text == "=":
                        buttons.setFixedSize(width_equal_button,
                                            height_equal_button)
                        layout.addWidget(buttons, row, column, 2, 1)
                    elif text == "Back": 
                        layout.addWidget(buttons, row, column, 1, 2)
                    else:
                        buttons.setFixedSize(default_size,
                                            default_size)
                        layout.addWidget(buttons, row, column)

                    # Is it a DEL, AC or equal button?
                    # if it is, add special function to them
                    if text == "=":
                        buttons.clicked.connect(self.process_input)
                    elif text == "ANS":
                        buttons.clicked.connect(self.get_the_previous_answer)
                    elif text == "AC":
                        buttons.clicked.connect(self.clear)
                    elif text == "DEL":
                        buttons.clicked.connect(self.delete)
                    elif text == "Back":
                        buttons.clicked.connect(self.go_back_to_main_window)
                    else:
                        buttons.clicked.connect(
                            lambda _, x=str(text): self.add_number(x)
                            )  

        # adding layout to main window
        layout.addLayout(input_label, 0,0 ,1, 4)
        self.setLayout(layout)

    def add_number(self, num):
        """Enter the number corresponding to the pressed button"""
        if self.line_edit.text() == self.error_message:
            self.line_edit.setText("")

        current_text = self.line_edit.text()
        self.line_edit.setAlignment(Qt.AlignLeft)
        self.line_edit.setText(current_text + num)
    
    def process_input(self):
        """process the input and print the output"""
        try:
            # Align the line edit and use eval() function to process inputs
            self.line_edit.setAlignment(Qt.AlignRight)
            self.answer = round(eval(self.line_edit.text()), 2)
            self.line_edit.setText(str(self.answer))

        except (NameError, SyntaxError, TypeError, ZeroDivisionError ):
            self.line_edit.setText(self.error_message)
    
    def get_the_previous_answer(self):
        """recall the previous output"""
        try:
            # Align the text in line edit and set current_text
            self.line_edit.setAlignment(Qt.AlignLeft)
            current_text = self.line_edit.text()

            # Is there the answer that is not deleted?
            # if yes, then set current_text to empty space
            if current_text == str(self.answer):
                current_text = ""
            new_text_display = current_text + str(self.answer)
            self.line_edit.setText(new_text_display)
            
        except AttributeError:
            self.line_edit.setAlignment(Qt.AlignRight)
            self.line_edit.setText(self.error_message)

    def delete(self):
        """delete one letter each time it is pressed"""
        # Is it a "ERROR!!!" message?
        # if yes, clear it
        if self.line_edit.text() == self.error_message:
            self.line_edit.clear()

        # if no, delete one letter each time the button is pressed
        else:
            current_text = self.line_edit.text()
            new_text = current_text[:-1]
            self.line_edit.setText(new_text)

    def clear(self):
        """Clear the text in the line edit"""
        self.line_edit.clear()

    
    def go_back_to_main_window(self):
        self.parent.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorAppWindow()
    window.show()
    sys.exit(app.exec())
