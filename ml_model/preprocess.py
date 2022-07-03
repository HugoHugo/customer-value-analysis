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
gdp_df['state'] = gdp_df['state'].apply(lambda x: x.lstrip().rstrip("\u202f*"))
# %%
gdp_df['gdp_per_capita'] = gdp_df['gdp_per_capita'].apply(lambda x: x.lstrip("$").replace(",", ""))
# %%
train_df = df
train_df = train_df.drop("State", axis=1)
#%%
train_df["state_gdp_percapita"] = df["State"].apply(lambda state:  gdp_df[gdp_df['state'] == state]["gdp_per_capita"].values[0])
train_df["state_gdp_percapita"] = train_df["state_gdp_percapita"].astype(int)
# %%
train_df.head()
# %%
# the higher the more monetary value
coverage_levels = dict(
    Basic=1,
    Extended=2,
    Premium=3
)
# %%
train_df["Coverage"] = train_df["Coverage"].apply(lambda cov: coverage_levels[cov])
# %%
train_df.head()
# %%
# encode unemployed as less monetary value
train_df["EmploymentStatus"] = train_df["EmploymentStatus"].apply(lambda x: int(x != 'Unemployed') + 1)
# %%
train_df.head()
# %%
train_df["Income"].describe()
# %%
predictive_columns = [
    "state_gdp_percapita",
    "Coverage", 
    "EmploymentStatus",
    "Income"]
# %%
target_column = "Customer Lifetime Value"
# %%
train_df[[target_column] + predictive_columns].head()
# %%
