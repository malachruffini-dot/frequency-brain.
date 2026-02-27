from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from datetime import datetime
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    matrix_labels = [
        "Solar Flux (F10.7)", "Magnetopause Standoff", "Schumann Resonance",
        "Seismic LF Noise", "Red Heifer Status", "Temple Altar Metrics",
        "Euphrates Flow Rate", "Euphrates GPR Voids", "Dead Sea Freshness",
        "CBDC Adoption %", "Biometric ID Rate", "Abrahamic Accord Status",
        "Skyquake Resonance", "Animal Die-off Coords", "Giza Sub-Siphon"
    ]
    
    data = []
    for label in matrix_labels:
        pe = round(random.uniform(0.75, 0.99), 2)
        # Generate a Delta (Change) between -0.05 and +0.05
        delta = round(random.uniform(-0.05, 0.05), 3)
        data.append({
            "text": label,
            "pe": pe,
            "delta": delta,
            "status": "FRESH" if random.random() > 0.2 else "STALE",
            "source": "Forensic Node " + str(random.randint(100, 999))
        })
    
    return {
        "hour_pos": 0.94,
        "min_pos": 0.22,
        "data": data,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
