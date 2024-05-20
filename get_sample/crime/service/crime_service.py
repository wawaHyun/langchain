
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crime.model.crime_model import CrimeModel
import pandas as pd


class CrimeService:
    def __init__(self):
        self.data = CrimeModel()
        this = self.data
        this.dname = './data/'
        this.sname = './save/'

    def get_sname(self):
        return self.data.sname

    def new_dframe_idx(self, fname: str) -> object:
        this = self.data
        return pd.read_csv(f'{this.dname}{fname}', index_col=0)

    def new_dframe(self, fname: str) -> object:
        this = self.data
        return pd.read_csv(f'{this.dname}{fname}')

    def save_model(self, fname: str, dframe: pd.DataFrame):
        this = self.data
        dframe.to_csv(f'{this.sname}{fname}', sep=',', na_rep='NaN')