import pandas as pd

# List of input files with the correct 'data/' folder path
files = [
    'data/daily_sales_data_0.csv', 
    'data/daily_sales_data_1.csv', 
    'data/daily_sales_data_2.csv'
]
processed_dfs = []

for file in files:
    # Read the CSV
    df = pd.read_csv(file)
    
    # 1. Filter for pink morsels only
    df = df[df['product'] == 'pink morsel']
    
    # 2. Convert price to float (removing the '$' sign)
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    
    # 3. Calculate sales (price * quantity)
    df['sales'] = df['price'] * df['quantity']
    
    # 4. Filter for the required columns
    df = df[['sales', 'date', 'region']]
    
    processed_dfs.append(df)

# Combine all dataframes into one
final_df = pd.concat(processed_dfs, ignore_index=True)

# Sort by date
final_df = final_df.sort_values('date')

# Save to the final output file
final_df.to_csv('formatted_sales_data.csv', index=False)

print("Data processing complete! Saved to formatted_sales_data.csv")