import math
while True:
    ch=int(input("\n1.square \n2.fact \n3.power \n4.ceil \n5.abs \n6.floor \n7.log \n8.log 10 \n9.pi val \n10.e value\n"))
    if ch==1:
        print(math.sqrt(25))
    elif ch==2:
        print(math.factorial(5))
    elif ch==3:
        print(math.pow(5,2))
    elif ch==4:
        print(math.ceil(4.5))
    elif ch==5:
        print(math.fabs(-10))
    elif ch==6:
        print(math.floor(1.5))
    elif ch==7:
        print(math.log(1))
    elif ch==8:
        print(math.log10(1))
    elif ch==9:
        print(math.pi)
    elif ch==10:
        print(math.e)
