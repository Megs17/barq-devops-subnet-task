FROM python:3.10-slim

WORKDIR /app

COPY subnet_analyzer.py visualize.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV INPUT_FILE=ip_data.xlsx

CMD python /app/subnet_analyzer.py && python /app/visualize.py
