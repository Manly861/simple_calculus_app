from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nhập liệu từ Button")

        # 1. Tạo ô nhập liệu
        self.line_edit = QLineEdit()
        
        # 2. Tạo các nút bấm
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")
        btn5 = QPushButton("5")
        btn6 = QPushButton("6")
        btn7 = QPushButton("7")
        btn8 = QPushButton("8")
        btn9 = QPushButton("9")
        btn0 = QPushButton("0")

        # 3. Kết nối sự kiện (Dùng lambda để truyền giá trị)
        btn1.clicked.connect(lambda: self.add_number("1"))
        btn2.clicked.connect(lambda: self.add_number("2"))
        btn3.clicked.connect(lambda: self.add_number("3"))
        btn4.clicked.connect(lambda: self.add_number("4"))
        btn5.clicked.connect(lambda: self.add_number("5"))
        btn6.clicked.connect(lambda: self.add_number("6"))
        btn7.clicked.connect(lambda: self.add_number("7"))
        btn8.clicked.connect(lambda: self.add_number("8"))
        btn9.clicked.connect(lambda: self.add_number("9"))
        btn0.clicked.connect(lambda: self.add_number("0"))
    

        # 4. Layout
        layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()



        
        h_layout.addWidget(btn1)
        h_layout.addWidget(btn2)
        h_layout.addWidget(btn3)
        h_layout_1.addWidget(btn4)
        h_layout_1.addWidget(btn5)
        h_layout_1.addWidget(btn6)
        h_layout_2.addWidget(btn7)
        h_layout_2.addWidget(btn8)
        h_layout_2.addWidget(btn9)
        h_layout_3.addWidget(btn0)


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
