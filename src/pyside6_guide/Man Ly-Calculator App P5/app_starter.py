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
        greeting_text = "This is the basic Calculator App. Enjoying It!"
        greeting = QLabel(greeting_text)
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
        layout.addWidget(greeting)
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
        self.review_layout.addStretch()
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
        user_input = self.input_label.text()
        try:
            # Check where is the arithmetic operation (+, -, * or x, / or :)
            math_op = ["+", "-", "*", "x", "/", ":"]
            operation = ""
            op_count = 0
            operation_index = 0
            check_point = 0

            # Is the input a negative number?
            # if yes, set the starting point of checking at 1 
            if (user_input.count("-") > 1 
                or user_input.find("-") == 0):
                check_point = 1
            
            # Foor loops to identify the operation and its index in input
            for index in range(check_point, len(user_input)):
                if user_input[index] in math_op:
                    operation = user_input[index]
                    operation_index = index
                    break

            # Identify where is number and where is operation
            str_a = user_input[ : operation_index]
            str_b = user_input[operation_index + 1 : ]
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
            
            # Print the final result
            self.output_label.setText(f"Answer: {answer}")

        except (AttributeError, ZeroDivisionError):
            self.output_label.setText("ERROR!!!")
        except ValueError:
            self.output_label.setText("I AM SORRY")


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
        thanks_message = "<b><i>Thank You So Much!!!<i><b>"
        waiting_message = "<i> I'm waiting for your response :)<i>"
        if state == 2:
            self.not_like_box.setChecked(False)
            self.appreciation.setText(thanks_message)
        elif state == 0:
            self.appreciation.setText(waiting_message)

    def not_like_box_stage_change(self, state):
        thanks_message = "<b><i> Thank You For Enjoying It! <i><b>"
        waiting_message = "<i>Just Take Time! I'm waiting for you :)<i>"
        if state == 2:
            self.like_box.setChecked(False)
            self.appreciation.setText(thanks_message)
        elif state ==  0:
            self.appreciation.setText(waiting_message)

    def change_window(self):
        self.calculator_screen = CalculatorAppWindow(parent = self)
        self.calculator_screen.show()
        self.hide()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()