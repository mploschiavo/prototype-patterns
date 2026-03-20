FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY producer.py ./
COPY consumer.py ./
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENV PYTHONUNBUFFERED=1
ENV KAFKA_CLIENT_MODE=producer
ENTRYPOINT ["/entrypoint.sh"]
