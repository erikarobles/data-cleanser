import pandas as pd

def find_errors(row):
    error = False
    error_columns = []

    if row.isnull().any():
        error = True
        error_columns.append('Missing Value')

    return error, error_columns

# read CSV files
file = pd.read_csv('student_performance.csv')

combined_data = pd.concat([file], ignore_index=True)
error_rows = pd.DataFrame(columns=combined_data.columns)
error_rows['error_columns'] = None

# iterate over rows and check for errors
for index, row in combined_data.iterrows():
    has_error, error_columns = find_errors(row)
    if has_error:
        row_with_errors = row.copy()
        row_with_errors['error_columns'] = ', '.join(error_columns)
        error_rows = error_rows.append(row_with_errors, ignore_index=True)

# saving
error_rows.to_csv('missingvalues.csv', index=False)