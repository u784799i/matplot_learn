import matplotlib.pyplot as plt
import numpy as np

n=12
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
plt.bar(X,Y1)
plt.show()
