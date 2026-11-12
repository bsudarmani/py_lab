import numpy as np
import statistics as st

data=[]
for i in range(5):
    data.append(int(input(f"Enter the value:{i+1}")))

print(data)
while True:
    ch=int(input("\n1.Mean \n2.Median \n3.Mode \n4.Range \n5.standard deviation \n6.variance \n7.HarmonicRange \n8.Geometric Mean "))
    if ch==1:
        print(st.mean(data))
    elif ch==2:
        print(st.median(data))
    elif ch==3:
        print(st.mode(data))
    elif ch==4:
        print(max(data)-min(data))
    elif ch==5:
        print(st.stdev(data))
    elif ch==6:
        print(st.variance(data))
    elif ch==7:
        print(st.harmonic_mean(data))
    elif ch==8:
        print(st.geometric_mean(data))
    elif ch==10:
        print(st.multimode(data))
