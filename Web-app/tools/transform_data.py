import connection as cnn
import pandas as pd
from io import StringIO

def transform_csv_raw_to_table(data):
    return pd.read_csv(StringIO(data))

def resume_data(dataset):
    return dataset.describe()
