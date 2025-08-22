from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from app.interfaces.IPage import IPage
from typing import Union

class PageManager(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.__page_layout = QVBoxLayout()
        self.__current_page: Union[QWidget, None] = None
        self.__pages = {}
        
        self.setLayout(self.__page_layout)
        
    def add_page(self, page: IPage):
        page.set_manager(self)
        new_page = page.build()
        new_page.hide()
        
        self.__pages[page.get_name()] = new_page
        self.__page_layout.addWidget(new_page)
        
    def get_page(self, name: str) -> QLayout:
        return self.__current_page
    
    def open_page(self, name: str):
        if not name in self.__pages:
            raise NameError("Нет окна с указанным именем!")
        
        if self.__current_page is not None:
            self.__current_page.hide()
            
        self.__current_page = self.__pages[name]
        self.__current_page.show()