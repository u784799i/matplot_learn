import matplotlib.pyplot as plt
import numpy as np

n=500
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
T=np.arctan2(y,x)

plt.scatter(x,y,s=1,c=T,alpha=1)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.show()

