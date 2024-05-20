from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

rrr = kiwoom.GetMasterLastPrice("005930")

print(int(rrr))
print(type(rrr))