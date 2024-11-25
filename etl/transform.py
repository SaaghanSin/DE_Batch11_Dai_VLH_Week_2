import pandas as pd

def transform_data(data):
    df = pd.DataFrame([data])
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['utc_datetime'] = pd.to_datetime(df['utc_datetime'])
    return df