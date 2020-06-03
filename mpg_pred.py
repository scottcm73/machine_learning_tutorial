import pandas as pd
import numpy as np
import sklearn 
import os

data_path=os.path.join("resources", "auto_mpg.csv")

df=pd.read_csv(data_path, index_col=False)
print(df.head())