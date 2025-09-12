import pandas as pd
import numpy as np


data = pd.DataFrame({
    'A': np.random.randint(1, 100, 5),
    'B': np.random.randint(1, 100, 5),
    'C': np.random.randint(1, 100, 5)
})

print("Dataset:\n", data)


print(data.head(2))

print(data.info())

print(data.describe())