import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(0, 100, 10))
df2 = pd.DataFrame(np.random.randint(0, 100, 10))

df_sum = df1 + df2
print(df_sum)


df_partial_sum = df1.head(5) + df2.head(5)
print(df_partial_sum)
