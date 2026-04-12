import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget


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
        btn0.setFixedSize(30,30)
        btn0.clicked.connect(lambda: self.add_number("0"))
 
        btn_enter = QPushButton("=")
        btn_sum = QPushButton("+")
        btn_subtract = QPushButton("-")
        btn_multiply = QPushButton("x")
        btn_divide = QPushButton("/")
        btn_enter.clicked.connect(lambda: self.add_number("="))

        # 2. Tạo các nút bấm
        # for in in range
        for i in range(9):
            number_button = QPushButton(str(i+1))
            number_button.setFixedSize(30,30)
            number_button.clicked.connect(lambda _, x=str(i+1): self.add_number(x))
            if i < 3:
                h_layout.addWidget(number_button)
            elif i == 2:
                h_layout.addWidget(btn_multiply)
            elif i < 6:
                h_layout_1.addWidget(number_button)
            elif i == 5:
                h_layout_1.addWidget(btn_divide)
            else:
                h_layout_2.addWidget(number_button)

        # keep
       
    

        h_layout_3.addWidget(btn0)
        
        #keep
        h_layout_3.addWidget(btn_enter)
        
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

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
