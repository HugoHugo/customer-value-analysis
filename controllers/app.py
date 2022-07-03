
from ml_model.train import training_function
from ml_model.predict import predict_clv
from ml_model.preprocess import load_and_preprocess

predictive_columns = [
        "state_gdp_percapita",
        "Coverage", 
        "EmploymentStatus",
        "Income"]

target_column = "clv"

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

def predict_clv_endpoint(request):
    customer_id = request["customer_id"]
    customer_data = request["data"]
    
    model_path = "../model.jbl"
    clv_prediction = predict_clv(customer_data, model_path)

    return {
        "customer_id": customer_id,
        "clv_prediction":clv_prediction
        }, 200