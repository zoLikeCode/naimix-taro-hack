FROM python:3.10.11
WORKDIR /app


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./api.py /app/
COPY ./tarot.py /app/
COPY prompts/ /app/prompts/
COPY ./server.py /app/


CMD ["python", "server.py"]