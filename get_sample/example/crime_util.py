
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import pandas as pd
from example.crime_abstract import PrinterBase, ReaderBase, ScraperBase, EditorBase
from icecream import ic
import googlemaps
from selenium import webdriver

class Editor(EditorBase):
    def dropna(self,this:pd.DataFrame)->pd.DataFrame:
        this.dropna(axis=0, inplace=True)

class Printer(PrinterBase):
    def dframe(self, this:pd.DataFrame) -> None:
        ic('*'*100)
        ic(f'타입 : {type(this)}')
        ic(f'column : {this.columns}')
        ic(f'top 1 col : {this.head(1)}')
        ic(f'null count : {this.isnul().sum()} 개')
        ic('*'*100)


class Reader(ReaderBase):
    def __init__(self):
        pass

    def csv(self,file) -> object:
        return pd.read_csv(f'{file}',encoding='UTF-8', thousands=',')
    
    def excel(self,file,header,usecols) -> object:
        return pd.read_excel(f'{file}', header=header, usecols=usecols)

    def json(self,file) -> object:
        return json.load(open(f'{file}.json',encoding='UTF-8'))
    
    def gmaps(self, api_key:str) -> object:
        return googlemaps.Client(key=api_key)

class Scraper(ScraperBase):
    def __init__(self):
        pass

    def driver(self, driver, url, selector, data) -> None:
        return webdriver.Chrome('')

    def auto_login(self, driver, url, selector, data) -> None:
        driver.get(url)
        driver.find_element_by_css_selector(selector).send_keys(data)
        driver.find_element_by_css_selector(selector).submit()