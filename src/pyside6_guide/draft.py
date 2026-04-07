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
        instruction = QLabel("This is the basic Calculator App. Click The Button Below To Start!")
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
        if "+" in self.input_label.text() :
            num_a = float(self.input_label.text()[ : (self.input_label.text().find("+"))])
            num_b = float(self.input_label.text()[(self.input_label.text().find("+")) + 1 : ])

            output = str(num_a + num_b)
        elif self.plus_input_label.text() == "-":
            output = str(num_a - num_b)
        elif self.plus_input_label.text() == "x":
            output = str(num_a * num_b)
        elif self.plus_input_label.text() == "/":
            output = str(num_a / num_b)
        else:
            output = "Warning"
        
        self.output_label.setText(f"Answer: {output}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()