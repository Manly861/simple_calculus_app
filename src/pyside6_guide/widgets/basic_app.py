"""
basic_app.py
by HundredVisionsGuy
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic App: a simple greeting app.")

        # TODO: add a text input for user's name
        self.username_input = QLineEdit(placeholderText="Enter Your Name Here.")

        # TODO: add a push button to greet user
        sumbit_button = QPushButton("Submit")
        sumbit_button.clicked.connect(self.get_input)

        # TODO: add a label to greet user
        self.instruction = "First, you may enter your name and then click the buttonn!"
        self.output_label = QLabel(self.instruction)

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.username_input)
        layout.addWidget(sumbit_button)
        layout.addWidget(self.output_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def get_input(self):
        """Get and process inout's information"""
        output = ""
        name = self.username_input.text()
        # Did user enter name?
        if not name:
            output = "Warning"
        else:
            output = f"Your name is {name}"

        self.output_label.setText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()