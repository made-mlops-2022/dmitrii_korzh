FROM python:3.7.4
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade pip && pip3 install -r requirements.txt --no-cache-dir

COPY utils app/utils
COPY models app/models
COPY app.py app/app.py

WORKDIR /app

CMD uvicorn app:app --host 0.0.0.0 --port 8001