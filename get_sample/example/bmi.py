
from utils import Member, memberlist, myRandom

class BMI():
    member = Member()

    def __init__(self) -> None:
        '''utils.py / Members(), myRandom() 를 이용하여 BMI 지수를 구하는 계산기를 작성합니다.'''

    def getgetBMI(self, height, weight) :
        this = self.member
        print(f'여기까지 ㅇㅋ')
        this = self.create_rows(this)
        print(f'여기까지 ㅇㅋ')

        print(f'여기까지 ㅇㅋ')
        print(f'this : ', this)
        print(f'{this.member.columns}')
        return this
    
    @staticmethod
    def create_rows(this) -> object :
        print("create_rows ㅇㅋ")
        print(this)
        for i in memberlist():
            print("name ",i)
            this['name'] = i,
            this['height'] = myRandom(130, 199),
            print("height ",this.height)
            this['weight'] = myRandom(40, 99)
            print("weight ",this.weight)
            # member.append({'name': name, 
            #                'height': myRandom(130, 199),
            #                'weight': myRandom(40, 99)})
        print("member ",this.name)
        return this
    
    # @staticmethod
    # def create_height(this) -> object :
    #     names = this
    #     print(f'names ',names)
    #     for i in names:
    #         print(f'i :',i.name)
    #         i['height'] = myRandom(130,199)
    #         print(i['height']& i['name'])
    #     return this
    
    # @staticmethod
    # def create_weight(this) -> object :
    #     this.weight = myRandom(120,190)
    #     return this

    def getBMI(self):
        '''BMI 지수를 계산합니다.'''
        this = Member()
        this.name = '홍길동'
        this.height = 170.8
        this.weight = 80.5
        res = this.weight / this.height**2 * 10000

        if res > 25:
            return f'{this.name}님은 비만입니다.'
        
