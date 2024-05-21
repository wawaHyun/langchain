
from dataclasses import dataclass
import pandas as pd


@dataclass
class CrimeDataset:
    _dname : str = ''
    _sname : str = ''
    _fname : str = ''
    _cctv : str = ''
    _crime : str = ''
    _pop : str = ''
    _police : str = ''
    _unemployment : str = ''
    _id : str = ''
    _label : str = ''
   
    @property
    def dname(self) -> str : return self._dname
    @dname.setter
    def dname(self, dname: str) : self._dname = dname
    @property
    def sname(self) -> str: return self._sname
    @sname.setter
    def sname(self, sname: str): self._sname = sname
    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname: str): self._fname = fname

    @property
    def cctv(self) -> str: return self._cctv
    @cctv.setter
    def cctv(self, cctv: pd.DataFrame): self._cctv = cctv

    @property
    def pop(self) -> str: return self._pop
    @pop.setter
    def pop(self, pop: pd.DataFrame): self._pop = pop

    @property
    def crime(self) -> str: return self._crime
    @crime.setter
    def crime(self, crime: pd.DataFrame): self._crime = crime

    @property
    def police(self) -> str: return self.police
    @police.setter
    def police(self, police: pd.DataFrame): self._police = police

    @property
    def unemployment(self) -> str: return self._unemployment
    @unemployment.setter
    def unemployment(self, unemployment: pd.DataFrame): self._unemployment = unemployment


    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id: str): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self,label: str): self._label = label

    def new_dataframe_with_index(self, fname: pd.DataFrame) -> pd.DataFrame:
        this = self.ds
        # index_col=0 해야 기존 index 값이 유지된다. 
        # 0은 컬럼명 중에서 첫번째를 의미한다.(배열구조)
        # pd.read_csv(f'경로/파일명/csv',index_col=0 => 인덱스로 지정할 column 명) index 지정
        return pd.read_csv(f'{this.dname}{fname}',index_col=0)    