
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from example.crime_util import Reader
from crime.model.crime_dataset import CrimeDataset
from crime.model.crime_model import CrimeModel

import pandas as pd
from konlpy.tag import Kkma, Komoran, Okt, Hannanum
from icecream import ic
import re
import konlpy
import nltk
import tweepy
from dotenv import load_dotenv
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('*' *100)
# print(BASE_DIR)
load_dotenv(os.path.join(BASE_DIR, ".env"))
'''
문제정의 !
서울시의 범죄현황과 CCTV현황을 분석해서
정해진 예산안에서 구별로 다음해에 배분하는 기준을 마련하시오.
예산금액을 입력하면, 구당 할당되는 CCTV 카운터를 자동으로
알려주는 AI 프로그램을 작성하시오.
'''

class CrimeService : 
    dataset = CrimeDataset()
    model = CrimeModel()

    def __init__(self) :
        # self.okt = Okt()
        self.data = self.dataset
        this = self.data
        this.dname = 'C:\\Users\\bitcamp\\TuringTeamPJT\\langchain\\get_sample\\crime\\data\\'
        this.sname = 'C:\\Users\\bitcamp\\TuringTeamPJT\\langchain\\get_sample\\crime\\save\\'
        this.cctv = 'cctv_in_seoul.csv'
        this.crime = 'crime_in_seoul.csv'
        self.crime_rate_columns = ['살인검거율','살인검거율','강도검거율','강간검거율','절도검거율','폭력검거율']
        self.crime_columns = ['살인','강도','강간','절도','폭력']
        self.arrest_columns = ['살인검거','강도검거','강간검거','절도검거','폭력검거']

    def process(self) -> object:
        this = self.dataset
        this.crime = self.crime_dataframe()
        this.cctv = self.cctv_dataframe()
        ic(this.crime.head())
        ic(this.cctv.head())
        this.police = self.save_police_position()
        ic('여기여기 : ', this.police)


    def crime_dataframe(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.data.dname}{self.data.crime}', encoding='UTF-8', thousands=',')
    
    def cctv_dataframe(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.data.dname}{self.data.cctv}', index_col=0)

    def save_police_position(self) -> None:
        station_names = []
        crime = self.crime_dataframe()
        for name in crime['관서명'] :
            station_names.append('서울'+str(name[:-1])+'경찰서')
        station_address = []
        station_lats = [] # 위도
        station_lngs = [] # 경도
        reader = Reader()
        gmaps = reader.gmaps(os.environ["api_key"])
        for name in station_names :
            t = gmaps.geocode(name, language='ko')
            print(t)
            station_address.append(t[0].get('formatted_address'))
            t_loc = t[0].get("geometry")
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])

        gu_names = []
        for name in station_address :
            tmp = name.split()
            tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
            gu_names.append(tmp_gu)
        
        crime['구별'] = gu_names
        # 구 와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] =='혜화서',['구별']] = '종로구'
        crime.loc[crime['관서명'] =='서부서',['구별']] = '은평구'
        crime.loc[crime['관서명'] =='강서서',['구별']] = '양천구'
        crime.loc[crime['관서명'] =='종암서',['구별']] = '성북구'
        crime.loc[crime['관서명'] =='방배서',['구별']] = '서초구'
        crime.loc[crime['관서명'] =='수서서',['구별']] = '강남구'
        ic(f'{self.data.sname}police_position.csv')
        crime.to_csv(f'{self.data.sname}police_position.csv')




if __name__ == "__main__" :
    crime = CrimeService()
    # ic(crime.crime_dataframe())
    # ic(crime.cctv_dataframe())
    crime.save_police_position()
