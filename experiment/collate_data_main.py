import pandas as pd
import numpy as np

# Define the file paths
excel_file = 'sample/master_dataset.xlsx'
output_file = 'sample/master_dataset.jsonl'

all_variants = []

# Helper function to safely construct the image path
def fix_image_path(row, variant_num):
    # Only modify if the image cell is not empty/NaN
    if pd.notna(row['image']) and str(row['image']).strip() != "":
        subject = str(row['subject']).strip()
        # Convert Excel backslashes to standard forward slashes
        img_path = str(row['image']).replace('\\', '/')
        return f"{variant_num:02d}/{subject}/{img_path}"
    
    # If no image, return None (which becomes 'null' in JSON)
    return None

for i in range(10):
    sheet_name = f'Instance_{i:02d}'
    print(f"Processing {sheet_name}...")
    
    try:
        # FIX 1: Read all data as strings (dtype=str) to prevent Excel from 
        # messing up numerical answers or dropping zeros.
        df = pd.read_excel(excel_file, sheet_name=sheet_name, dtype=str)
        
        # FIX 2: Strip any accidental hidden spaces in the column names
        df.columns = df.columns.str.strip()
        
        # Add the 'variant' column (as an integer)
        df.insert(2, 'variant', i) 
        
        # Convert string 'nan' values back to actual nulls
        df.replace({'nan': np.nan, 'NaN': np.nan, 'None': np.nan}, inplace=True)
        
        # FIX 3: Apply our safe image path function row-by-row
        if 'image' in df.columns:
            df['image'] = df.apply(lambda row: fix_image_path(row, i), axis=1)
        
        all_variants.append(df)
    except ValueError:
        print(f"Warning: Sheet {sheet_name} not found in Excel file.")

# Concatenate all sheets into one massive dataframe
master_df = pd.concat(all_variants, ignore_index=True)

# Export to JSONL
# force_ascii=False ensures Arabic, Chinese, etc., stay as actual characters, not unicode \uXXXX garble
master_df.to_json(output_file, orient='records', lines=True, force_ascii=False)

print(f"Success! Saved combined data to {output_file}")