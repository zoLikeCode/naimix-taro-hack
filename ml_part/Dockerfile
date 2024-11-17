FROM python:3.10.11
WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
#RUN gigachain install-rus-certs || true

COPY . .


CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8002"]