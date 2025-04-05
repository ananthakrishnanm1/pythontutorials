import pandas as pd

data = {'Name': ['Tom', 'Nick', 'John'], 'Age': [10, 15, 20]}
df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)
