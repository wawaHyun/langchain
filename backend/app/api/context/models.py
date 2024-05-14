import pandas as pd
from app.api.context.data_sets import DataSets


class Models:
    def __init__(self) -> None:
      self.ds = DataSets()
      this = self.ds
      this.dname = './data'
      this.sname = './save'


    def new_model(self,fname) -> object:
        this = self.ds
        # index_col=0 해야 기존 index값이 유지됌
        # 0 은 컬럼명 중에서 첫번째를 의미함.
        # pd.read_csv(f'경로/파일명/csv', index_col=0 = '인덱스로 지정할 column명') Index 지정

        return pd.read_csv(f'{this.dname}{fname}', index_col=0) # 0:행, 1:열
   
    def new_dframe(self,fname) -> object:
        this = self.ds
        # pd.read_csv('경로/파일명.csv') Index를 지정하지 않음.
        return pd.DataFrame(f'{this.dname}{fname}')
   
    def seve_model(self, fname, dframe) -> object : 
       this = self.ds
       '''
       풀옵션은 다음과 같다
       df.to_csv(f'{self.ds.sname}{fname}',sep=',',na_rep='NaN',
                         float_format='%.2f',  # 2 decimal places
                         columns=['ID', 'X2'],  # columns to write
                         index=False)  # do not write index
        na = 잘못된 값
        NaN = not a number. 숫자가 아니다.
        rep = replace
       '''
       return dframe.to_csv(f'{this._dname}{fname}', sep=',', na_rep='NaN') # 0:행, 1:열
   
   