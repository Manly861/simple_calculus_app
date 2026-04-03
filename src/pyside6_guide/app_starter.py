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
        instruction = "This is the basic Calculator App. Click The Button Below To Start!"
        self.output_label = QLabel(instruction)

        # create a button
        enter_button = QPushButton("Enter")


        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.output_label)
        layout.addWidget(enter_button)


        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()