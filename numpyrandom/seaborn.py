import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()




from numpy import random

x = random.normal(size=(2, 3))

print(x)

import seaborn as sns 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data)