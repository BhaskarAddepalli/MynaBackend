import csv
from collections import deque 


#  ABC -> (2,10.06,500) ()
#   DEF ->

class Person:
  def __init__(self, time, symbol, side,price,quantity):
    self.time =time
    self.symbol=symbol
    self.side=side
    self.price=price
    self.quantity=quantity



with open('/Users/gurusaiaddepalli/Downloads/demo_trades.csv') as file:
    csv_reader=csv.reader(file,delimiter='\t')
    Dict ={}
    lst=[]
    ans=0
    # print(Dict['ABC'].get())
    for row in csv_reader:
        string_list = row[0].split(",") if row else []
        lst.append(string_list);
    lst.pop(0)
    for l in lst:
        print(l)
        # print()
        # print()
        # print()
        if(l[2] == 'B'):
            if l[1] not in Dict:               
                que=[Person(l[0],l[1],l[2],l[3],l[4])]
                # print(que[0])
                Dict[l[1]]=que
            elif Dict[l[1]][0].quantity > 0:
                # print("2")
                print(que[0])
                Dict[l[1]].append(Person(l[0],l[1],l[2],l[3],l[4]))
            else:
                required=int(l[4])
                # print("3")
                print(l)
                while len(Dict[l[1]]) >0 and required>0:
                    temp1=int(Dict[l[1]][0].quantity)
                    s1=float(Dict[l[1]][0].price)
                    s2=float(l[3]);
                    if abs(temp1) <= required:
                        
                        # q1=int(temp1)
                        print(Dict[l[1]][0].time,l[0],l[1],abs(temp1),  temp1*s1+(-1)*temp1*s2,'S','B',Dict[l[1]][0].price,l[3])
                        ans+=temp1*s1+(-1)*temp1*s2
                        Dict[l[1]].pop(0)
                        required-=abs(temp1)
                    else:

                        print(Dict[l[1]][0].time,l[0],l[1],abs(required),-1*required*s1+required*s2,'S','B',Dict[l[1]][0].price,l[3])
                        ans+=(-1*required*Dict[l[1]][3]+required*l[3])
                        Dict[l[1]][0].quantity = temp1+required
                        required-=abs(temp1)

        elif l[2]=='S':
            if Dict.get(l[1]) ==None :
                # print('adi')
                que=[Person(l[0],l[1],l[2],l[3],-1*l[4])]
                Dict[l[1]]=que
            elif Dict[l[1]][0].quantity < 0:
                Dict[l[1]].append(Person(l[0],l[1],l[2],l[3],-1*l[4]))
            else:
                required=int(l[4])
                #  500 200 300 ,600
                while len(Dict[l[1]]) >0 and required>0:
                    temp1=int(Dict[l[1]][0].quantity)
                    s1=float(Dict[l[1]][0].price)
                    s2=float(l[3]);
                    print("adi")
                    if abs(temp1) <= required:
                        # print(Dict[l[1]])
                        print(Dict[l[1]][0].time,l[0],l[1],abs(temp1),temp1*s1+(-1)*temp1*s2,'S','B',Dict[l[1]][0].price,l[3])
                        
                        ans+=temp1*s1+(-1)*temp1*s2
                        Dict[l[1]].pop(0)
                        required-=abs(temp1)
                    else:
                        print(Dict[l[1]][0].time,l[0],l[1],abs(required),-1*required*s1+required*s2,'S','B',Dict[l[1]][0].price,l[3])
                        ans+=(-1*required*s1+required*s2)
                        Dict[l[1]][0].quantity = str(temp1+required)
                        required-=abs(temp1)
    print(ans)

    