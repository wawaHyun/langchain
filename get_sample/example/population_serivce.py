
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from example.crime_util import Reader
from crime.model.crime_dataset import CrimeDataset
from crime.model.pop_model import PopModel
import pandas as pd
from icecream import ic



class PopService : 
    dataset = CrimeDataset()
    model = PopModel()

    def __init__(self) :
        self.data = self.dataset
        this = self.data
        this.dname = 'C:\\Users\\bitcamp\\TuringTeamPJT\\langchain\\get_sample\\crime\\data\\'
        this.sname = 'C:\\Users\\bitcamp\\TuringTeamPJT\\langchain\\get_sample\\crime\\save\\'
        this.pop = 'pop_in_seoul.xls'
        self.pop_columns = "B:B,D:D,G:G,J:J,N:N"
        self.pop_rows = ['B2','D2','G2','J2','N2']
        # self.pop_columns = ['자치구','합계','한국인','등록외국인','65세이상고령자']

    def process(self) -> object:
        this = self.dataset
        ic('여기여기')
        this.pop = self.pop_dataframe()
        ic(this.pop)
        # this.police = self.save_police_position()
        # ic('여기여기 : ', this.police)


    def pop_dataframe(self) -> pd.DataFrame:
        return pd.read_excel(f'{self.data.dname}{self.data.pop}', header=1, usecols=self.pop_columns, skiprows=1)
    

    def save_pop_seoul(self) -> None:
        station_names = []
        pop = self.pop_dataframe()
        
        pop.to_csv(f'{self.data.sname}police_position.csv')


if __name__ == "__main__" :
    pop = PopService()
    pop.process()

