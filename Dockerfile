FROM python:3.10
WORKDIR /app
COPY controllers/ /app/controllers/
COPY ml_model/ /app/ml_model/
COPY gdp-perstate-wikipedia.csv /app/
COPY model.jbl /app/
COPY WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv /app/
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
ENV FLASK_APP "/app/controllers/app.py"
CMD [ "flask", "run" ]