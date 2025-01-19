import pandas
import duckdb
import seaborn as sns
import matplotlib.pyplot as plt

data = pandas.read_csv(r"E:\Personal Projects\RAW DATA\Zomato-data-.csv")
print(data)

def null_finder(x):
                if x.isnull().values.any():
                    print("The file contains null data")
                else:
                    print("No null data found")
#null_finder(data)

sns.countplot(x=data['online_order'])
plt.show()

