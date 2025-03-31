import pandas as pd

def create_dataframe_with_index(data, index_labels):
  df = pd.DataFrame(data, index=index_labels)
  return df

data1 = [['Alice', 25, 'Engineer'],
         ['Bob', 30, 'Teacher'],
         ['Charlie', 22, 'Student']]
index1 = ['Person A', 'Person B', 'Person C']
df1 = create_dataframe_with_index(data1, index1)
print("DataFrame 1:")
print(df1)
print("-" * 20)
