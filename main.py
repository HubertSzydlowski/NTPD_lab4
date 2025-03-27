from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import numpy as np
from sklearn.linear_model import LinearRegression

# Inicjalizacja aplikacji
app = FastAPI()

# Zadanie 1: Stworzenie podstawowej aplikacji API

@app.get("/")
def read_root():
    return {"message": "Witaj w API FastAPI!"}

# Zadanie 2: Dodanie modelu ML i endpointu predykcji
# Zadanie 3: Obsługa błędów i walidacja danych

# Przykładowe dane do trenowania modelu regresji
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([2, 4, 6, 8, 10])

# Trenowanie prostego modelu regresji liniowej
model = LinearRegression()
model.fit(X_train, y_train)

# Definiowanie modelu danych wejściowych dla predykcji
class PredictionInput(BaseModel):
    x: float

@app.post("/predict")
def predict(data: PredictionInput):
    try:
        x_value = float(data.x) 
        prediction = model.predict([[x_value]])
        return {"prediction": prediction[0]}
    except ValueError:
        raise HTTPException(status_code=400, detail="Niepoprawny format liczby.")

# Zadanie 4: Rozszerzenie API o dodatkowe endpointy i dokumentację

@app.get("/info")
def get_model_info():
    return {
        "model_type": type(model).__name__,  # Pobiera dynamicznie typ modelu
        "num_features": model.coef_.shape[0],  # Pobiera liczbę cech modelu
        "trained_on": len(X_train),  # Pobiera liczbę próbek użytych do treningu
        "coefficients": model.coef_.tolist(),  # Współczynniki modelu
        "intercept": model.intercept_,  # Punkt przecięcia osi Y
    }

@app.get("/health")
def health_check():
    try:
        # Prosta kontrola, czy model może zrobić predykcję
        test_value = np.array([[0]])
        _ = model.predict(test_value)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Zadanie 5: Uruchomienie aplikacji w trybie produkcyjnym
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False, workers=4)