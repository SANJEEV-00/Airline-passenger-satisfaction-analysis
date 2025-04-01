import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('airline.csv')
# Customer satisfaction distribution
sns.countplot(x='satisfaction', data=df)
plt.show()