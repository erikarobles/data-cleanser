import pandas as pd

# Function to identify inconsistencies or errors in a row
def find_errors(row):
    # Define your custom error-checking logic here
    # For example, check if a value is an outlier or if a string is incorrectly formatted
    error = False
    error_columns = []

    if row['Marks'] > 100 or row['Marks'] < 0:  # Replace 'column_name' and 'threshold' with your specific case
        error = True
        error_columns.append('Marks')

    # Add more error-checking conditions if necessary
    if row['Effort_Hours'] < 0:
        error = True
        error_columns.append('Effort_Hours')

    if row.isnull().any():
        error = True
        error_columns.extend(row[row.isnull()].index.tolist())

    return error, error_columns

# Read CSV files
file4 = pd.read_csv('file (4).csv')

# Combine all files into a single DataFrame
# combined_data = pd.concat([file1, file2, file3, file4], ignore_index=True)
combined_data = pd.concat([file4], ignore_index=True)
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