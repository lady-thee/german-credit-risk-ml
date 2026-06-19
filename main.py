import pandas as pd
import numpy as np
import matplotlib.pyplot as mplt
import seaborn as sbn
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

df = pd.read_csv(BASE_DIR / "data" / "german_credit_data.csv")

print(df.shape)
