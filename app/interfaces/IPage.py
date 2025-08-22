from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from abc import ABC, abstractmethod

class IPage(ABC):
    
    @abstractmethod
    def build(self) -> QWidget:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def set_manager(self, manager):
        pass
    
    @abstractmethod
    def get_manager(self):
        pass