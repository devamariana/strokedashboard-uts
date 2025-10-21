import pandas as pd
import os

def clean_data():

    # Pastikan folder data_clean sudah ada

    os.makedirs("data_clean", exist_ok=True)

    # Baca data mentah

    df = pd.read_csv("data/healthcare-dataset-stroke-data.csv")

    # Bersihkan data

    df = df.drop_duplicates()

    df = df.dropna()

    # Simpan ke folder data_clean

    df.to_csv("data_clean/stroke_clean.csv", index=False)

    return df