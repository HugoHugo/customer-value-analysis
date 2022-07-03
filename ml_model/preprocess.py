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
gdp_df = pd.read_csv("../gdp-perstate-wikipedia.csv")
# %%
gdp_df['state'] = gdp_df['state'].apply(lambda x: x.rstrip("*"))
# %%
gdp_df['gdp_per_capita'] = gdp_df['gdp_per_capita'].apply(lambda x: x.lstrip("$").replace(",", ""))
# %%
