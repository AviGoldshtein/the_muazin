FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY services/data_loader_src services/data_loader_src
COPY services/shared services/shared

CMD ["python", "-m", "services.data_loader_src.main"]
