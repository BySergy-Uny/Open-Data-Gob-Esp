import connection as cnn
import pandas as pd
from io import StringIO

# Definitions

def transform_csv_raw_to_table(data):
    return pd.read_csv(StringIO(data))

def resume_data(dataset):
    return dataset.describe()

# Uses and examples

data = str(cnn.data, 'utf-8')
transform_data = transform_csv_raw_to_table(data)
print(transform_data.head())
print("resume \n---\n", resume_data(transform_data))
