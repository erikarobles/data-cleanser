import pandas as pd

# Function to identify inconsistencies or errors in a row
def find_errors(row):
    # Define your custom error-checking logic here
    # For example, check if a value is an outlier or if a string is incorrectly formatted
    error = False
    error_columns = []

    # Check if Department_ID rows are unique
    if len(row['Department_ID'].unique()) != len(row['Department_ID']):
        error = True
        error_columns.append('Department_ID')
    
    # Check if Department_Name rows are unique
    if len(row['Department_Name'].unique()) != len(row['Department_Name']):
        error = True
        error_columns.append('Department_Name')
    
    # Check if DOE rows GREATER or equal to 1900
    if row['DOE'] < 1900:
        error = True
        error_columns.append('DOE')
    
    # Check for missing values
    

    return error, error_columns

# Read CSV files
data = pd.read_csv('department.csv')

# Combine all files into a single DataFrame
# combined_data = pd.concat([file1, file2, file3, file4], ignore_index=True)
combined_data = pd.concat([data], ignore_index=True)
# Remove duplicates


# Handle missing values (e.g., fill with the mean or median)
# combined_data['column_name'].fillna(combined_data['column_name'].mean(), inplace=True)

# # Standardize date format
# combined_data['date'] = pd.to_datetime(combined_data['date'], format='%Y-%m-%d')

# Initialize a DataFrame to store the rows with errors
error_rows = pd.DataFrame(columns=combined_data.columns)
error_rows['error_columns'] = None

# Iterate over the rows in the combined_data DataFrame and check for errors
for index, row in combined_data.iterrows():
    has_error, error_columns = find_errors(row)
    if has_error:
        row_with_errors = row.copy()
        row_with_errors['error_columns'] = ', '.join(error_columns)
        error_rows = error_rows.append(row_with_errors, ignore_index=True)

# Save the rows with errors to a CSV file
error_rows.to_csv('error_rows.csv', index=False)