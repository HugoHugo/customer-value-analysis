FROM python:3.10
WORKDIR /app
ADD controllers /app/
ADD ml_model /app/
ADD gdp-perstate-wikipedia.csv /app/
ADD model.jbl /app/
ADD WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv /app/
RUN pip3 install -r requirements.txt