
from ml_model.train import training_function
from ml_model.predict import predict_clv
from ml_model.preprocess import load_and_preprocess

from flask import Flask
from flask import request

app = Flask(__name__)

predictive_columns = [
        "state_gdp_percapita",
        "Coverage", 
        "EmploymentStatus",
        "Income"]

target_column = "clv"

@app.route("/train_model")
def train_model_endpoint(request):
    train_filepaths = request["train_filepaths"]
    gdp_filepath = request["gdp_filepath"]
    train_df = load_and_preprocess(train_filepaths, gdp_filepath)
    
    model = training_function(
        train_df,
        predictive_columns,
        target_column)
    
    is_model = bool(model)
    
    return is_model, 200 if is_model else 500

@app.route("/predict_clv")
def predict_clv_endpoint():
    customer_id = request.json["customer_id"]
    customer_data = request.json["data"]

    model_path = "model.jbl"
    clv_prediction = predict_clv([customer_data], model_path)

    return {
        "customer_id": customer_id,
        "clv_prediction": clv_prediction[0].round()
        }, 200

@app.route("/authed_predict_clv")
def authed_predict_clv_endpoint():
    if not request.headers.get("Authorization") == "Bearer weak-password-use-secrets-instead":
        return {}, 403
    
    customer_id = request.json["customer_id"]
    customer_data = request.json["data"]

    model_path = "model.jbl"
    clv_prediction = predict_clv([customer_data], model_path)

    return {
        "customer_id": customer_id,
        "clv_prediction": clv_prediction[0].round()
        }, 200