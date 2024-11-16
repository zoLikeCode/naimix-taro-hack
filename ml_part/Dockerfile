FROM python:3.10.11
WORKDIR /app


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY prompts/ /app/prompts/
COPY json/ /app/json/
COPY ./server.py /app/


CMD ["python", "server.py"]