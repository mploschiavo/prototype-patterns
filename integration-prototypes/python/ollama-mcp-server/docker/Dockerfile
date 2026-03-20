FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
COPY rag-documents.json ./
ENV PYTHONUNBUFFERED=1
ENV PORT=8090
EXPOSE 8090
CMD ["python", "app.py"]
