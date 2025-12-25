import numpy as np
l=np.random.randint(25,50,14)
print(l)
l1=l[l>=35]
print("Heat wave days:",l1)
print("Number of heat wave days:",len(l1))
l[l<30]=30
print("Replace temperatures below 30c",l)
l2=l[(l<=34) & (l>=30)]
print("Comfortable days:",l2)
print("Increase all heat-wave day temperatures by 2c",l1+2)