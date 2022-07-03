#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import neighbors
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
train_df = train_df.rename({"Customer Lifetime Value":"clv"},axis=1)
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
target_column = "clv"
# %%
X = train_df[predictive_columns].to_numpy()
y = train_df[target_column].to_numpy()
# %%
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.25, random_state=525)

# %%
reg = LinearRegression().fit(X_train, y_train)
reg.score(X_test, y_test)
# %%
array_of_mses = []
for n_neighbors in range(2,15):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights="uniform")
    fitted_model_knn = knn.fit(X_train, y_train)
    y_pred = fitted_model_knn.predict(X_test)
    # compute MSE
    knn_mse = pow(sum(y_test - y_pred) / y_test.shape[0], 2)
    array_of_mses.append((knn_mse,n_neighbors))
# %%
array_of_mses.sort()
best_nearest_neighbor = array_of_mses[0][1]
print("best_nearest_neighbor", best_nearest_neighbor)
# %%
