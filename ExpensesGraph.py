import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
#print(df)

expenses = df['Food'] + df['Transportation'] + df['Rent']

plt.pie(expenses, labels=('March', 'April', 'December'), autopct='%1.1f%%')
plt.title('Monthly Expenses')
plt.show()
