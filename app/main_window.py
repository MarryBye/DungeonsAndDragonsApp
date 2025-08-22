from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

from app.pages.new_char_page import NewCharPage
from app.pages.table_page import TablePage
from app.pages.choose_page import ChoosePage
from app.page_manager import PageManager

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.window_manager = PageManager()
        
        self.setCentralWidget(self.window_manager)
        
        self.window_manager.add_page(NewCharPage(name="create_char_page"))
        self.window_manager.add_page(TablePage(name="table_page"))
        self.window_manager.add_page(ChoosePage(name="choose_page"))
        
        self.window_manager.open_page("choose_page")
        
        