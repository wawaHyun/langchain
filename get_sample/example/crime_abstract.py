from abc import *
import pandas as pd

class EditorBase(metaclass=ABCMeta):
    @abstractmethod
    def dropna(self,this:pd.DataFrame)->pd.DataFrame:
        this = this.dropna()
        return this

class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def excel(self):
        pass

    @abstractmethod
    def json(self):
        pass

    @abstractmethod
    def gmaps(self):
        pass

class ScraperBase(metaclass=ABCMeta):
    @abstractmethod
    def driver(self):
        pass

