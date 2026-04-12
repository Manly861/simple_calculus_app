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
    QGridLayout,
    QWidget,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic Calculus Apps")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 200)

        layout = QGridLayout()
        title_label = QLabel("Welcome User To Calculus App!")

        # create a label 
        instruction = QLabel("This is the basic Calculator App. Enjoying It!")
        self.input_label = QLineEdit(placeholderText= "Enter A Number Here")
        self.answer = "Answer:"
        self.output_label = QLabel(self.answer)

        # create a button
        enter_button = QPushButton("=")
        enter_button.clicked.connect(self.process_input)
        num_1_button = QPushButton("1")
        num_2_button = QPushButton("2")
        num_3_button = QPushButton("3")

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(instruction)
        layout.addWidget(self.input_label)
        layout.addWidget(self.output_label) 
        layout.addWidget(enter_button)
        layout.addWidget(num_1_button, 0, 0)
        layout.addWidget(num_2_button, 0, 1)
        layout.addWidget(num_3_button, 0, 2)
        # [OPTIONAL] Add a stretch to move everything up
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    

    def process_input(self):
        """process the input and mathematical function"""
        try:
            answer = eval(self.input_label.text())
            self.output_label.setText(f"Answer: {answer}")
        except NameError and SyntaxError:
            self.output_label.setText("ERROR!!!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()