import pandas as pd

# Read the first csv file into a pandas dataframe
df1 = pd.read_csv('counceling.csv')

# Read the second csv file into another pandas dataframe
df2 = pd.read_csv('department.csv')

# Merge the two dataframes using a left join
results = df1[~df1['Department_Admission'].isin(df2['Department_ID'])]

# Save the results dataframe to a new csv file
results.to_csv('dept_id_mismatches.csv', index=False)