FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY services/speech_to_text services/speech_to_text
COPY services/shared services/shared

CMD ["python", "-m", "services.speech_to_text.main"]
