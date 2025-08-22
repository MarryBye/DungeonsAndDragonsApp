from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from app.pages.base_page import BasePage

class NewCharPage(BasePage):
    def build(self):
        page = QWidget()
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        manager = self.get_manager()
        
        name_input = QLineEdit()
        drive_input = QLineEdit()
        
        form_layout.addRow("Name: ", name_input)
        form_layout.addRow("Drive: ", drive_input)
        
        btn_back = QPushButton("Back")
        btn_back.clicked.connect(lambda: manager.open_page("choose_page"))
        
        main_layout.addLayout(form_layout)
        main_layout.addWidget(btn_back)
        page.setLayout(main_layout)
        
        return page