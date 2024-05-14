



from app.api.context.data_sets import DataSets
from app.api.context.models import Models


class TitanicModel(object):
    model = Models()
    dataset = DataSets()

    def preprocess(self, train_fname, test_fname) -> object:
        this = self.dataset
        this = self.model

        this.ds.train = self.new_model(train_fname)
        this.ds.test = self.new_model(test_fname)
        feature = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
        # dataset은 train과 test, validation 3종류로 나뉘어져 있다.
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train.drop(['Survived'], axis=1)
        this = self.drop_feature(this,'Name','SibSp','Parch','Ticket','Cabin')

        return this.dataset

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
    
    @staticmethod
    def extract_title_from_name(this) -> None:
        return this

    @staticmethod
    def title_nominal(this) -> None:
        return this