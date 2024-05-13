from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd

class TitanicService:

    model = TitanicModel()

    def process(self):
        print(f'process start!')
        this = self.model
        this.train = self.new_model('train.csv')
        this.test = self.new_model('test.csv')
        print(f'tranin cols : {this.train.columns}')
        print(f'test cols : {this.test.columns}')
        this.id = this.test['PassengerId']
        print('ㅇㅋ!')

        this = self.drop_feature(this,'Name','SibSp','Parch','Ticket','Cabin')
        print('ㅇㅋ!')
        self.df_info(this)
        print('ㅇㅋ!')
        print(f'tranin tiket drop cols : {this.train.columns}')
        print(f'test tiket drop cols : {this.test.columns}')

        return this.train.columns
    
        # this = self.create_tranin(this)

    
    def new_model(self,payload) -> object:
        this = self.model
        this._context = './app/api/titanic/data/'
        this._fname = payload
        return pd.read_csv(this._context + this._fname)
    
    @staticmethod
    def df_info(this) :
        # for i in [this.train, this,text]:
        #     print(this.train.head())
        #     print(this.test.head())
        [i.info() for i in [this.train, this.test]]

    @staticmethod
    def create_tranin(this) -> str : 
        print(f'create_tranin진입')
        return this.tranin.drop('Survived', axis=1) # axis:축, 0:행, 1:열

    @staticmethod
    def create_label(this) -> str : 
        print(f'create_label진입')
        return this.tranin['Survived']

    @staticmethod
    def drop_feature(this,*feature) -> object :
        # inplace=false로 되어있는 for문 (외부반복)
        # for i in feature:
        #     this.train = this.train.drop(i, axis=1)
        #     this.test = this.test.drop(i, axis=1)

        # for i in [this.train, this.test]:
        #     for j in feature :
        #         i.drop(j, axis=1, inplace=True)

        # inplace=true로 되어있는 for문 (내부반복)
        [i.drop(j, axis=1, inplace=True)for j in feature for i in [this.train, this.test]]


        return this
    