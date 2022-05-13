
fname = "original.txt"
f = open(fname,"r")
SetC = set()
while True:
    line = f.readline()
    if not line: break
    line = line.strip()
    SetC.add(line)
f.close() 
li = [] 
for x in SetC:
    li.append(x)
import random
import time
print("푸실 문제의 갯수를 선택하세요")
Dcount = input()
print("엔터를 치면 시작됩니다.")

countt = 0 
def m1():
    input()
    start = time.time()
    print(start)
    def m2():   
      if input()==d:
       global countt      
       countt+=1 
       print("{}번째 문제 정답입니다.".format(x+1))
      else:
       print("틀렸습니다.")
       inputt = input("다음 문제로 가고싶습니까?(y) :" )
       if inputt in [ "y" , "Y"]:
          print("다음 문제로 갑니다.")
       else:   
         print(d)
         m2()
    for x in range(int(Dcount)):
      d = random.choice(li)
      print(d)
      m2()
    end = time.time()
    print(end-start)
    print("총 {} 개 맞추었습니다.".format(countt))
m1()

