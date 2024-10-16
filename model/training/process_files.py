# Utility script to process the files in the EMG_data_for_gestures-master folder

import pandas as pd
from pathlib import Path

folder = Path('./EMG_data_for_gestures-master')

# Get all the folders in the directory
folders = [f for f in folder.iterdir() if f.is_dir()]

# Get all the files in the folders
files = [f for folder in folders for f in folder.iterdir() if f.is_file()]

for file in files:
    # Reading the data into a DataFrame, assuming the gaps are spaces
    df = pd.read_csv(file, delim_whitespace=True)

    # Dropping the 'time' column
    df = df.drop(columns=['time'])

    # Saving the modified DataFrame as a CSV
    output_csv_path = f'./data/{file.stem}.csv'
    df.to_csv(output_csv_path, index=False)