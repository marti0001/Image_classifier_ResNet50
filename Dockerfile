# wybiera bazowy obraz dockera z pythonem 3.9 w wersji slim
FROM python:3.9-slim

#tworzy katalog /app i ustawia go jako domyslnąlokalizajce dla kolejnych komend
WORKDIR /app

# kopiuje plik requirements.txt z twojego komputera do katalogu /app w kontenerze w celu przygotowania zaleznosci do instalacji
COPY requirements.txt .

# Instaluje pythonowe zależności z pliku requirements.txt, przygotowuje srodowisko i usuwa pobrane pliki w celu oszczednosci miejsca
RUN pip install --no-cache-dir -r requirements.txt

# Kopiuje całą zawartość bieżącego katalogu (gdzie znajduje się Dockerfile) do kontenera
COPY . .

# Deklaruje, że kontener nasłuchuje na porcie 8080
EXPOSE 8080

# Uruchamia serwer Uvicorn z Twoją aplikacją FastAPI , server ASGI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
