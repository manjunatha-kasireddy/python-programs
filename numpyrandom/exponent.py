# from numpy import random
# x = random.exponential(scale=2, size=(2, 3))
# print(x)

from numpy import random
x = random.chisquare(df=2, size=(2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()

from numpy import random
x = random.rayleigh(scale=2, size=(2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

from numpy import random
x = random.pareto(a=2, size=(2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()

from numpy import random
x = random.zipf(a=2, size=(2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show()