FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0"]

