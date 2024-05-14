import numpy as np
from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd
import icecream as ic

class TitanicService:

    model = TitanicModel()

    def process(self):
        print(f'process start!')
        this = self.model

        this.train = self.new_model('train.csv')
        this.test = self.new_model('test.csv')

        print(f'tranin cols : {this.train.columns}')
        print(f'test cols : {this.test.columns}')

        this.feature = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
        this = self.PassengerId_odinal(this)
        this = self.Survived_interval(this)
        this = self.pclass_odinal(this)
        this = self.Sex_interval(this)
        this = self.Age_ratio(this)
        this = self.Fare_ratio(this)
        this = self.Embarked_nominal(this)

        this.id = this.test['PassengerId']

        
        this = self.drop_feature(this,'Name','SibSp','Parch','Ticket','Cabin')
        self.df_info(this)

        print(f'tranin tiket drop cols : {this.train.columns}')
        print(f'test tiket drop cols : {this.test.columns}')

        # this = self.create_tranin(this)
        return "process!"
    

    
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
    def extract_title_from_name(this) -> pd.DataFrame:
        for i in [this.trein, this.test] : 
            i['title'] = i['name'].str.extract('([A-Za-z]+)\.', expend=False)
        return this
    
    @staticmethod
    def remove_duplicate_title(this) -> pd.DataFrame:
        a= []
        for this in [this.train, this.test]:
            a += list(set(these['title']))
        a = list(set(a))
        print(a)
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr':1,'Ms':2,'Mrs':3,'Master':4,'Royal':5,'Rare':6}
        return title_mapping
    
    @staticmethod
    def title_nominal(this, title_mapping) -> pd.DataFrame:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this
    
    @staticmethod
    def name_nominal(this) -> pd.DataFrame:
        return this

    @staticmethod
    def PassengerId_odinal(this)-> pd.DataFrame:
        this.train = this.train({})
        return this
    
    @staticmethod
    def Survived_interval(this)-> pd.DataFrame:
        return this
    
    @staticmethod
    def pclass_odinal(this)-> pd.DataFrame:
        return this

    @staticmethod
    def Sex_interval(this)-> pd.DataFrame:
        return this

    @staticmethod
    def Age_ratio(this)-> pd.DataFrame:
        train =this.train
        test =this.test
        age_mapping = {'Unknown':0 , 'Baby': 1, 'Child': 2, 'Teenager' : 3, 'Student': 4,
                       'Young Adult': 5, 'Adult':6,  'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5) # fillna는 DataFrame에서 결측값을 원하는 값으로 변경시킴.
        test['Age'] = test['Age'].fillna(-0.5) # NaN 값에 -0.5를 할당하여 Unknown으로 pd.cut될수 있게 함.
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # bins(히스토그램 bins)의 인접값을 이용해 pd.cut 구간을 나눔. np.inf = 무한대
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior'] # bins(box)의 구간의 이름
        
        for these in train, test : 
            these['Age'] = pd.cut(these['Age'], bins, labels=labels) # bins 구간을 기준으로 labels에 cut하여 넣음.
            these['AgeGroup'] = these['Age'].map(age_mapping) # labels의 값에 따라서 age_mapping과 mapping 함.
        return this
    
    @staticmethod
    def Fare_ratio(this)-> pd.DataFrame:
        return this
    
    @staticmethod
    def Embarked_nominal(this)-> pd.DataFrame:
        return this
    
