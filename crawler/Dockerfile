FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl && \
    pip install --no-cache-dir flask playwright && \
    playwright install

COPY app.py /app/app.py
WORKDIR /app

CMD ["python", "app.py"]
