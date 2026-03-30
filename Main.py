from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "project": "F1 Tracker"}

@app.get("/races")
def get_races():
    return [
        {"id": 1, "name": "Bahrain Grand Prix", "season": 2024, "round": 1},
        {"id": 2, "name": "Saudi Arabian Grand Prix", "season": 2024, "round": 2},
        {"id": 3, "name": "Australian Grand Prix", "season": 2024, "round": 3},
    ]
@app.get("/drivers")
def get_drivers():
    return [
        {"id": 1, "name": "Max Verstappen", "team": "Red Bull", "number": 1},
        {"id": 2, "name": "Lewis Hamilton", "team": "Ferrari", "number": 44},
        {"id": 3, "name": "Lando Norris", "team": "McLaren", "number": 4},
    ]