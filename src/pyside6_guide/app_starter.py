"""
app_starter.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QCheckBox,  
    QPushButton,
    QFrame,
)
from PySide6.QtCore import Qt
from calculator_app_screen import CalculatorAppWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set main window and layout
        self.setWindowTitle("Basic Calculus Apps")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 200)

        layout = QVBoxLayout()
        self.review_layout = QHBoxLayout()
        title_label = QLabel("Welcome User To Calculus App!")

        # create labels and a line edit
        instruction = QLabel("This is the basic Calculator App. Enjoying It!")
        self.review_label = QLabel("Do You Like My Calculator?")
        self.review_label.setAlignment(Qt.AlignCenter)
        self.appreciation = QLabel("...")
        self.appreciation.setAlignment(Qt.AlignCenter)
        self.input_label = QLineEdit(placeholderText= "Enter A Number Here")
        self.answer = "Answer:"
        self.output_label = QLabel(self.answer)

        # Create a seperator line
        self.line_separator = QFrame()
        self.line_separator.setFrameShape(QFrame.HLine)

        # create a button
        enter_button = QPushButton("=")
        change_button = QPushButton("Change")
        enter_button.clicked.connect(self.process_and_enable)
        change_button.clicked.connect(self.change_window)

        # Create check boxes
        self.like_box = QCheckBox("Yes, I Like It", self)
        self.not_like_box = QCheckBox("No, I Don't Like It", self)
        self.like_box.stateChanged.connect(self.like_box_stage_change)
        self.not_like_box.stateChanged.connect(self.not_like_box_stage_change)

        # Hide the revirew layour in display
        self.line_separator.hide()
        self.review_label.hide()
        self.like_box.hide()
        self.not_like_box.hide()
        self.appreciation.hide()


        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(instruction)
        layout.addWidget(self.input_label)
        layout.addWidget(self.output_label) 
        layout.addWidget(enter_button)
        layout.addWidget(change_button)

        # Add review title and line separator
        layout.addWidget(self.line_separator)
        layout.addWidget(self.review_label)
        
        # Add review layout (check boxes and appreciate message)
        layout.addLayout(self.review_layout)
        self.review_layout.addWidget(self.like_box)
        self.review_layout.addWidget(self.not_like_box)
        layout.addWidget(self.appreciation)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
        
    def process_input(self):
        """process the input and mathematical function"""
        try:
            # Check where is the arithmetic operation (+, -, * or x, / or :)
            operation = ""
            operation_index = 0
            starting_check_point = 0
            if self.input_label.text().count("-") > 1:
                starting_check_point = 1
            
            for index in range(starting_check_point, len(self.input_label.text())):
                if self.input_label.text()[index] in ["+", "-", "*", "x", "/", ":"]:
                    operation = self.input_label.text()[index]
                    operation_index = index
                    break

            # Identify where is number and where is operation
            str_a = self.input_label.text()[ : operation_index]
            str_b = self.input_label.text()[operation_index + 1 : ]
            num_a = float(str_a)
            num_b = float(str_b)

            # Is it a summation?
            if operation == "+":
                answer = str(num_a + num_b)

            # Is it a subtraction?
            elif operation == "-":
                answer = str(num_a - num_b)

            # Is it a multiplication?
            elif operation == "*" or operation == "x":
                answer = str(num_a * num_b)

            # Is it a division?
            elif operation == "/" or operation == ":" :
                answer = str(num_a / num_b)

            else:
                answer = "ERROR!!!"
            
            # Print the final result
            self.output_label.setText(f"Answer: {answer}")
        except (ValueError, AttributeError):
            self.output_label.setText("ERROR!!!")

    def enable_check_box(self):
        """Enable the review layout"""
        self.line_separator.show()
        self.review_label.show()
        self.like_box.show()
        self.not_like_box.show()
        self.appreciation.show()

    def process_and_enable(self):
        self.process_input()
        self.enable_check_box()

    def like_box_stage_change(self, state):
        if state == 2:
            self.not_like_box.setChecked(False)
            self.appreciation.setText("<b><i>Thank You So Much!!!<i><b>")
        elif state == 0:
            self.appreciation.setText("<i> I'm waiting for your response :) <i>")

    def not_like_box_stage_change(self, state):
        if state == 2:
            self.like_box.setChecked(False)
            self.appreciation.setText("<b><i> Thank You For Enjoying It! <i><b>")
        elif state ==  0:
            self.appreciation.setText("<i>Just Take Time! I'm waiting for your response :)<i>")

    def change_window(self):
        self.calculator_screen = CalculatorAppWindow(parent = self)
        self.calculator_screen.show()
        self.hide()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()