FROM python:3.8-slim

COPY src/counter-incrementer-service.py /app/counter-incrementer-service.py

WORKDIR /app

CMD ["python", "counter-incrementer-service.py"]
