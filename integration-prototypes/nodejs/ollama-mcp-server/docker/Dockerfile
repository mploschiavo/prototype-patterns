FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN if [ -f package-lock.json ]; then npm ci --omit=dev --no-audit --no-fund; else npm install --omit=dev --no-audit --no-fund; fi
COPY app.js ./
COPY rag-documents.json ./
ENV PORT=8090
EXPOSE 8090
CMD ["node", "app.js"]
