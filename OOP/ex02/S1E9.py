from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def is_alive_method(self):
        return self.is_alive


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)