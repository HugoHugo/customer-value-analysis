#%%
import pandas as pd
# %%
df = pd.read_csv("../WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv")
# %%
df.head()
# %%
# do we have one row per customer 
df["Customer"].unique().shape[0] == df["Customer"].shape[0]
# %%
