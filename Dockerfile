# Używamy lekkiego obrazu Python 3.9
FROM python:3.9-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Skopiowanie plików aplikacji do kontenera
COPY main.py /app/
COPY requirements.txt /app/

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Otworzenie portu dla aplikacji
EXPOSE 8000

# Uruchomienie aplikacji FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]