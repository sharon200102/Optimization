import numpy as np
import pandas as pd
rows = ["Company 1", "Company 2", "Company 3", "Company 4", "Company 5"]
columns = ["Food", "Clothing", "Sound", "Scenery", "Cleaning"]
dataset = np.random.randint(100, high=1000, size=(5, 5), dtype='l')
data = pd.DataFrame(dataset, index=rows, columns=columns)
data.to_csv('optimization data')
