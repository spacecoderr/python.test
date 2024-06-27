import numpy as num
import matplotlib.pyplot as plt
langs={"C","Java","Python"}
votes=[10.0,20.0,50.0]
explodes=[0.0,0.3,0.0]

plt.pie(votes,labels=langs,explode=explodes,autopct="%.2f%%")
plt.show()