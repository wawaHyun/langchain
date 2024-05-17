
from utils import myRandom


class RPS:

    def __init__(self) -> None:
        print(f'utils.py myRandom() 를 이용하여 가위바위보 객체를 생성합니다')

    # def play(self):
    #     c = myRandom(1,3)
    #     p = input('가위', '바위', '보')
    #     # 1: 가위, 2: 바위, 3: 보
    #     rps = ['가위', '바위', '보']
    #     if p == rps[c-1] :
    #         print(f'컴퓨터: {rps[c-1]}, 당신 : {p}, 비겼습니다.')
    #     elif p == rps[c % 3] :
    #         print(f'컴퓨터: {rps[c-1]}, 당신 : {p}, 당신이 이겼습니다.')
    #     else : 
    #         print(f'컴퓨터: {rps[c-1]}, 당신 : {p}, 컴퓨터가 이겼습니다.')
    
    if __name__ == "__main__":
        c = myRandom(1,3)
        p = input[ 0:"가위", 1:"바위", 2:"보"]
        # 1: 가위, 2: 바위, 3: 보
        rps = ['가위', '바위', '보']
        if p == rps[c-1] :
            print(f'컴퓨터: {rps[c-1]}, 당신 : {p}, 비겼습니다.')
        elif p == rps[c % 3] :
            print(f'컴퓨터: {rps[c-1]}, 당신 : {p}, 당신이 이겼습니다.')
        else : 
            print(f'컴퓨터: {rps[c-1]}, 당신 : {p}, 당신이 졌습니다.')
    