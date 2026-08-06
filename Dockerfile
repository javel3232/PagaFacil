FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/ ./services/
COPY tests/ ./tests/
COPY version.json .

EXPOSE 8000

CMD ["python3", "-c", "import json; v=json.load(open('version.json')); print(f'PagaFacil v{v[\"major\"]}.{v[\"minor\"]}.{v[\"patch\"]} corriendo...')"]
