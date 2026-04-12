import sys
from PySide6.QtWidgets import (
    QApplication, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLineEdit, 
    QPushButton, 
    QWidget,
    QSizePolicy, 
    )


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nhập liệu từ Button")

        layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()

        # 1. Tạo ô nhập liệu
        self.line_edit = QLineEdit()
        btn0 = QPushButton("0")
        btn0.clicked.connect(lambda: self.add_number("0"))
        btn0.setFixedSize(30,30)

        # Operation
        btn_enter = QPushButton("=")
        btn_sum = QPushButton("+")
        btn_subtract = QPushButton("-")
        btn_multiply = QPushButton("x")
        btn_divide = QPushButton("/")

        # Function
        del_btn = QPushButton("DEL")
        clear_btn = QPushButton("CLEAR")

        # Special Operation
        dot_btn = QPushButton(".")
        percentage_btn = QPushButton("%")

        # adding click funtion
        btn_enter.clicked.connect(lambda: self.add_number("="))
        btn_sum.clicked.connect(lambda: self.add_number("+"))
        btn_subtract.clicked.connect(lambda: self.add_number("-"))
        btn_divide.clicked.connect(lambda: self.add_number("/"))
        btn_multiply.clicked.connect(lambda: self.add_number("*"))
        del_btn.clicked.connect(lambda: self.delete())
        clear_btn.clicked.connect(lambda: self.clear())
        dot_btn.clicked.connect(lambda: self.add_number("."))
        percentage_btn.clicked.connect(lambda: self.add_number("%"))

        btn_enter.setFixedSize(72, 30)
        btn_sum.setFixedSize(30,30)
        btn_subtract.setFixedSize(30,30)
        btn_divide.setFixedSize(30,30)
        btn_multiply.setFixedSize(30,30)



        # 2. Tạo các nút bấm
        # for in in range
        for i in range(9):
            # add number button
            number_button = QPushButton(str(i+1))
            number_button.setFixedSize(30,30)
            number_button.clicked.connect(lambda _, x=str(i+1): self.add_number(x))
            if i < 3:
                h_layout.addWidget(number_button)
            elif i < 6:
                h_layout_1.addWidget(number_button)
            else:
                h_layout_2.addWidget(number_button)

            # add operation button
            if i == 2:
                h_layout.addWidget(btn_multiply)
            elif i == 5:
                h_layout_1.addWidget(btn_divide)
            elif i == 8:
                h_layout_2.addWidget(btn_subtract)


        # adding layout 3 to window
        h_layout_3.addWidget(btn0)
        h_layout_3.addWidget(btn_enter)
        h_layout_3.addWidget(btn_sum)
        h_layout_3.addWidget(del_btn)
        h_layout_3.addWidget(clear_btn)
        h_layout_3.addWidget(dot_btn)
        h_layout_3.addWidget(percentage_btn)


        
        # adding layout to main window
        layout.addWidget(self.line_edit)
        layout.addLayout(h_layout)
        layout.addLayout(h_layout_1)
        layout.addLayout(h_layout_2)
        layout.addLayout(h_layout_3)
        
        self.setLayout(layout)

    def add_number(self, num):
        # Lấy chữ hiện tại + số mới nhấn
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text + num)

    def clear(self):
        self.line_edit.clear()
    
    def delete(self):
        current_text = self.line_edit.text()
        new_text = current_text[:-1]
        self.line_edit.setText(new_text)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
