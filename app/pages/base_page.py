from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from app.interfaces.IPage import IPage
from app.page_manager import PageManager

class BasePage(IPage):
    def __init__(self, name):
        
        self.__manager: PageManager = None
        self.__name: str = name
        
    def build(self):
        return super().build()
    
    def get_name(self):
        return self.__name
    
    def set_manager(self, manager: PageManager):
        self.__manager = manager
    
    def get_manager(self):
        return self.__manager