import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,50)
y=x**3
plt.figure(num=1)
plt.plot(x,y,label='2')


y1=x**2
plt.figure(num=1)
plt.plot(x,y1,color='red',linestyle='-',label='1')

plt.xlabel('x')
plt.yticks([0.1,0.5],['good','normal'])
ax=plt.gca()
ax.spines['right'].set_color('red')
ax.spines['bottom'].set_position(('data',-0.1))
plt.legend()
x0=1
y0=x0+1
plt.scatter(x0,y0,color='b')
plt.plot([x0,x0],[y0,0],'k--')
plt.show()

