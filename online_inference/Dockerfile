FROM python:3.10-slim

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY main.py app/main.py
COPY src app/src
COPY model app/model

WORKDIR /app
ENV PATH_TO_MODEL="model/model_lr.pkl"
ENV GDOWN_ID="1Noc5ld0vzXBGzL-6AXGUjToSy_q_VeO5"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8112"]