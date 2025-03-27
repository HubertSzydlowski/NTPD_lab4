# 1. Dodaj do swojego repozytorium krótkie instrukcje uruchamiania aplikacji: Lokalnie; Za pomocą Dockera; Za pomocą Docker Compose;

## Lokalnie

1. Upewnij się, że masz zainstalowanego Pythona (zalecana wersja 3.9) oraz zależności z pliku `requirements.txt`.

2. Zainstaluj wymagane biblioteki:
    ```
    pip install -r requirements.txt
    ```
3. Uruchom aplikację:
    ```
    uvicorn main:app --reload
    ```
4. Aplikacja będzie dostępna pod adresem: [http://localhost:8000](http://localhost:8000).

## Za pomocą Dockera

1. Zbuduj obraz Dockera:
    ```
    docker build -t fastapi-ml-app .
    ```
2. Uruchom kontener:
    ```
    docker run -d -p 8000:8000 fastapi-ml-app
    ```
3. Aplikacja będzie dostępna pod adresem: [http://localhost:8000](http://localhost:8000).

## Za pomocą Docker Compose

1. Upewnij się, że masz przygotowany plik `docker-compose.yml`. 

2. Uruchom aplikację za pomocą Docker Compose:
    ```
    docker-compose up -d
    ```
3. Aplikacja będzie dostępna pod adresem: [http://localhost:8000](http://localhost:8000).

---

# 2. Opisz, w jaki sposób skonfigurować parametry (np. zmienne środowiskowe) i jakich zasobów potrzebuje aplikacja;

## Zmienne środowiskowe

- REDIS_HOST: Adres hosta, na którym działa Redis. W przypadku używania Docker Compose, jest to `redis` (nazwa kontenera).
- REDIS_PORT: Port, na którym Redis nasłuchuje. Domyślnie to port `6379`.
      
## Zasoby potrzebne do aplikacji

- Redis: W przypadku, gdy aplikacja korzysta z Redis, będzie on wymagał dostępu do portu 6379. Zadbaj o to, by mieć zainstalowanego Redis-a lub kontener Redis.
- Pamięć: Aplikacja będzie wymagała odpowiedniej ilości pamięci operacyjnej, zwłaszcza jeśli zajmuje się dużymi danymi.
- Porty: Upewnij się, że port 8000 (lub inny, który wybierzesz) jest dostępny na twoim systemie.
