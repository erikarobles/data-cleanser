import pandas as pd

# Read data from the CSV file
file_path = "department.csv"  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Check for duplicate rows based on 'Student_ID' and 'Paper_ID'
duplicates = df.duplicated(subset=['Department_ID'], keep=False)

# Filter the DataFrame to include only the duplicated rows
duplicated_rows = df[duplicates]

# Check if any duplicates exist
if not duplicated_rows.empty:
    # Save the duplicated rows to a new CSV file
    duplicated_rows.to_csv("duplicated_rows.csv", index=False)
    print("Duplicated rows saved to duplicated_rows.csv")
else:
    print("There are no duplicates.")