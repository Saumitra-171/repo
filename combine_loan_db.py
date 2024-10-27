import pandas as pd

# Load the CSV files into DataFrames
csv1_df = pd.read_csv('ELECT Loan Data (1).csv')
csv2_df = pd.read_csv('ELECT_Loans_Database_Table.csv')


# Combine both DataFrames
combined_df = pd.concat([csv1_df, csv2_df], ignore_index=True)


# Set 'Loan_ID' as the index and handle duplicates or missing values
try:
    combined_df.set_index('Loan_ID', inplace=True)
    print("Successfully set 'Loan_ID' as the index.")
except KeyError:
    print("Error: 'Loan_ID' column is not found in the data.")
    # Optional: Inspect the combined data
    print(combined_df.head())


# Check for duplicate and missing values in the index if 'Loan_ID' is successfully set as the index
if combined_df.index.duplicated().any():
    print("Warning: There are duplicate Loan_ID values in the data.")
    combined_df = combined_df[~combined_df.index.duplicated(keep='first')]

if combined_df.index.isnull().any():
    print("Warning: There are missing Loan_ID values.")
    combined_df.dropna(subset=['Loan_ID'], inplace=True)


# Drop rows with missing 'Loan_ID' values
combined_df.dropna(subset=['Loan_ID'], inplace=True)
# Fill remaining missing values with a placeholder or the column’s median/mean
combined_df.fillna(value={'column_name': 'placeholder_value'}, inplace=True)


# Save the combined DataFrame if 'Loan_ID' indexing was successful
combined_df.to_csv('combined_file.csv')
print("Combined and cleaned data saved to 'combined_file.csv'.")