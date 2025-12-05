FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main_api.py .

COPY model/ ./model/

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main_api:app"]