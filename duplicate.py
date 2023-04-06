import pandas as pd

# read CSV file
file_path = "student_performance.csv"  
df = pd.read_csv(file_path)

duplicates = df.duplicated(subset=['Student_ID', 'Paper_ID'], keep=False)

duplicated_rows = df[duplicates]

# check for duplicates
if not duplicated_rows.empty:
    duplicated_rows.to_csv("duplicated_rows.csv", index=False)
    print("Duplicated rows saved to duplicated_rows.csv")
else:
    print("There are no duplicates.")