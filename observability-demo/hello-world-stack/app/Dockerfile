FROM python:3.12-slim

WORKDIR /app
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY app/app.py /app/app.py

ENV PORT=8080
ENV APP_LOG_DIR=/var/log/demo-app

EXPOSE 8080
CMD ["python", "/app/app.py"]
