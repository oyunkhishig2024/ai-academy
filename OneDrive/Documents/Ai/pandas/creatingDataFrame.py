import pandas as pd
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19],
        'City': ['New York', 'Paris', 'Berlin'],
        'Country': ['USA', 'France', 'Germany'],
        'Salary': [10000, 20000, 15000]
        }


        
df = pd.DataFrame(data)
print(df)
print(df['City'])