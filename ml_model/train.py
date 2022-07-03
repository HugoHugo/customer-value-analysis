import numpy as np
from sklearn import neighbors
from sklearn.model_selection import train_test_split

def hyperparameter_tune(
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_test: np.ndarray,
        y_test: np.ndarray
    ):
    array_of_mses = []
    for n_neighbors in range(2,10):
        knn = neighbors.KNeighborsRegressor(
            n_neighbors, weights="uniform"
        )
        fitted_model_knn = knn.fit(X_train, y_train)
        y_pred = fitted_model_knn.predict(X_test)
        # compute MSE
        knn_mse = sum(pow(y_test - y_pred, 2)) / y_test.shape[0]
        array_of_mses.append((knn_mse,n_neighbors))
    array_of_mses.sort()
    print(array_of_mses)


def train_model(
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_test: np.ndarray,
        n_neighbors: int
    ):
    knn = neighbors.KNeighborsRegressor(
        n_neighbors, weights="uniform"
    )
    fitted_model_knn = knn.fit(X_train, y_train)
    y_pred = fitted_model_knn.predict(X_test)
    return y_pred, fitted_model_knn

def training_function(train_df, predictive_columns, target_column):
    X = train_df[predictive_columns].to_numpy()
    y = train_df[target_column].to_numpy()

    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.25, random_state=525)

    optimal_n_neighbors = hyperparameter_tune(
        X_train,
        y_train,
        X_test,
        y_test
    )

    _, fitted_model_knn = train_model(
        X_train,
        y_train,
        X_test,
        optimal_n_neighbors
    )
    
    return fitted_model_knn