import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 28],
        'City': ['New York', 'Houston', 'Chicago', 'Houston', 'New York'],
        'Salary': [7000, 8000, 7500, 9000, 8500]
        }


df = pd.DataFrame(data)
print(df[['Name', 'City']])
print(df[['Name', 'Age', 'Salary']])