import pandas as pd
import os

# Define file paths
DATA_DIR = './data'
OUTPUT_FILE = './formatted_data.csv'


def process_data():
    print("Beginning data processing...")

    # 1. LOAD AND COMBINE DATA
    all_data = []
    # Loop through every file in the data folder
    for file_name in os.listdir(DATA_DIR):
        if file_name.endswith('.csv'):
            file_path = os.path.join(DATA_DIR, file_name)
            # Read the CSV
            df = pd.read_csv(file_path)
            all_data.append(df)
            print(f"Loaded {file_name}")

    # Stack all three files on top of each other
    merged_df = pd.concat(all_data, ignore_index=True)

    # 2. FILTER FOR "pink morsel"
    # The instructions say Soul Foods only cares about Pink Morsels
    merged_df = merged_df[merged_df['product'] == 'pink morsel']

    # 3. CREATE "sales" COLUMN
    # First, clean the price (remove '$' and convert to number)
    merged_df['price'] = merged_df['price'].str.replace('$', '').astype(float)

    # Calculate Sales = Quantity * Price
    merged_df['sales'] = merged_df['quantity'] * merged_df['price']

    # 4. SELECT COLUMNS
    # We only need Sales, Date, and Region
    final_df = merged_df[['sales', 'date', 'region']]

    # 5. EXPORT
    # Save to a new CSV file without the index numbers
    final_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Success! Processed data saved to {OUTPUT_FILE}")


# Execute the function
if __name__ == '__main__':
    process_data()