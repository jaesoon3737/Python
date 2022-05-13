import os
from typing import ItemsView


def RemoveDir(target):
    kids = os.listdir(target)
    kids.sort()
    for kid in kids:  
              kid2 = os.path.join(target,kid)   
              if os.path.isfile(kid2):
                  os.remove(kid2)   
              else:
                 kids2 = os.listdir(kid2)   
                 if len(kids2) == 0:
                     os.rmdir(kid2)
                 else:
                    RemoveDir(kid2)
    os.rmdir(target)
                  
                  
                  
target = input("리스팅할 디렉토리 :")

if os.path.exists(target):
    if os.path.isdir(target):
        print("존재함")
        RemoveDir(target)      
    else:
       print("존재안함")
else:
    print(target+"디렉토리가 존재하지 않음")
