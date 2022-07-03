from joblib import load

def predict_clv(X_test, model_path):
    knn = load(model_path)
    y_pred = knn.predict(X_test)
    return y_pred