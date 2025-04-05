import pandas as pd

data = [['Tom', 10], ['Nick', 15], ['John', 20]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df.set_index('Name', inplace=True)
print(df)
