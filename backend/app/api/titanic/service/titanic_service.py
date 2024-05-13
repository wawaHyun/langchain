from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd

class TitanicService:
    model = TitanicModel()

    def process(self):
        print(f'process start!')
        train_model = self.new_model('train.csv')
        test_model = self.new_model('test.csv')
        print(f'tranin col : {train_model.colums}')
        print(f'test col : {test_model.colums}')


    def new_model(self,payload) -> object:
        this = self.model
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
