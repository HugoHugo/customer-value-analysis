
from ml_model import train
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
    
    model = train.training_function(
        train_df,
        predictive_columns,
        target_column)
    
    return bool(model)