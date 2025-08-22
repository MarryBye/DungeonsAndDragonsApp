from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from app.pages.base_page import BasePage

class ChoosePage(BasePage):
    def build(self):
        page = QWidget()
        main_layout = QVBoxLayout()
        manager = self.get_manager()
        
        btn1 = QPushButton("First")
        btn1.clicked.connect(lambda: manager.open_page("create_char_page"))
        
        btn2 = QPushButton("Second")
        btn2.clicked.connect(lambda: manager.open_page("table_page"))
        
        btn3 = QPushButton("Third")     
        btn3.clicked.connect(lambda: manager.open_page("choose_page"))   
        
        main_layout.addWidget(btn1)
        main_layout.addWidget(btn2)
        main_layout.addWidget(btn3)

        page.setLayout(main_layout)
        
        return page