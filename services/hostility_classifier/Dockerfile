FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY services/hostility_classifier services/hostility_classifier
COPY services/shared services/shared

CMD ["python", "-m", "services.hostility_classifier.main"]
