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
    QWidget,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic Calculus Apps")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 200)

        layout = QVBoxLayout()
        title_label = QLabel("Welcome User To Calculus App!")

        # create a label 
        instruction = QLabel("This is the basic Calculator App. Enjoying It!")
        self.input_label = QLineEdit(placeholderText= "Enter A Number Here")
        self.answer = "Answer:"
        self.output_label = QLabel(self.answer)

        # create a button
        enter_button = QPushButton("=")
        enter_button.clicked.connect(self.process_input)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(instruction)
        layout.addWidget(self.input_label)
        layout.addWidget(self.output_label) 
        layout.addWidget(enter_button)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
        
    def process_input(self):
        """process the input and mathematical function"""
        try:
            # Check where is the arithmetic operation (+, -, *, /)
            operation = ""
            if "+" or "-" or "*" or "/" in self.input_label.text():
                for i in range(len(self.input_label.text())):
                    if not self.input_label.text()[i].isdigit():
                        operation = self.input_label.text()[i]
            
            # Identify where is number and where is operation
            str_a = self.input_label.text()[ : (self.input_label.text().find(operation))]
            str_b = self.input_label.text()[(self.input_label.text().find(operation)) + 1 : ]
            num_a = float(str_a)
            num_b = float(str_b)

            # Is it a summation?
            if operation == "+":
                output = str(num_a + num_b)

            # Is it a subtraction?
            elif operation == "-":
                output = str(num_a - num_b)

            # Is it a multiplication?
            elif operation == "x":
                output = str(num_a * num_b)

            # Is it a division?
            elif operation == "/":
                output = str(num_a / num_b)

            else:
                output = "Warning"
            
            # Print the final result
            self.output_label.setText(f"Answer: {output}")
        except ValueError:
            self.output_label.setText("ERROR!!!")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()