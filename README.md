# Customer Value Prediction API

Predicts the value of an IBM Watson-based customer based on multiple data points

## Source of Data

Customer Value dataset
```
https://www.kaggle.com/datasets/pankajjsh06/ibm-watson-marketing-customer-value-data
```
US States GDP per capita
```
https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_GDP
```

## Sample requests and responses

Request
```
curl --location --request GET 'http://127.0.0.1:5000/predict_clv' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_id": 456,
    "data": [
        1000000,
        1,
        1,
        1
    ]
}'
```
Response
```
{
    "clv_prediction": 4155.0,
    "customer_id": 456
}
```

Request
```
curl --location --request GET 'http://127.0.0.1:5000/predict_clv' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_id": 556,
    "data": [
        1000000,
        2,
        1,
        1
    ]
}'
```
Response
```
{
    "clv_prediction": 14745.0,
    "customer_id": 556
}
```

Request
```
curl --location --request GET 'http://127.0.0.1:5000/predict_clv' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_id": 656,
    "data": [
        1000000,
        2,
        1,
        10000
    ]
}'
```
Response
```
{
    "clv_prediction": 4703.0,
    "customer_id": 656
}
```

## Example Authentication
Request
```
curl --location --request GET 'http://127.0.0.1:5000/authed_predict_clv' \
--header 'Authorization: Bearer weak-password-use-secrets-instead' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_id": 156,
    "data": [
        100,
        1,
        2,
        1
    ]
}'
```
Response
```
{
    "clv_prediction": 7062.0,
    "customer_id": 156
}
```