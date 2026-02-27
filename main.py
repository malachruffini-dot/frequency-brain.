from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
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

def get_payload():
    # 'type' must be EXACTLY 'Hardware' or 'Grid' for the app columns to work
    matrix = [
        ("Solar Flux (F10.7)", "Hardware", "117.4Hz Bursts"),
        ("Magnetopause Standoff", "Hardware", "Source Leaks"),
        ("Schumann Resonance", "Hardware", "Freq Shift"),
        ("Seismic LF Noise", "Hardware", "Antediluvian"),
        ("Red Heifer Status", "Grid", "Temple Key"),
        ("Temple Altar Metrics", "Hardware", "Physical Ready"),
        ("Euphrates Flow Rate", "Hardware", "Buffer Removal"),
        ("Euphrates GPR Voids", "Hardware", "Exposed Voids"),
        ("Dead Sea Freshness", "Grid", "Salt-Seal"),
        ("CBDC Adoption %", "Grid", "Financial Lock"),
        ("Biometric ID Rate", "Grid", "Node Integ"),
        ("Abrahamic Accord Status", "Grid", "Geopolit Lock"),
        ("Skyquake Resonance", "Hardware", "Gate Fingerprint"),
        ("Animal Die-off Coords", "Hardware", "Pulse Test"),
        ("Giza Sub-Siphon", "Hardware", "Primary Infra")
    ]
    
    data = []
    for m in matrix:
        pe = round(random.uniform(0.75, 0.99), 2)
        data.append({
            "text": m[0],
            "type": m[1],
            "pe": pe,
            "status": "FRESH" if random.random() > 0.3 else "OLD",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "source": m[2]
        })
        
    convergence = round(random.uniform(0.90, 0.99), 4)
    return {
        "hour_pos": convergence,
        "min_pos": (convergence * 12) % 1.0,
        "data": data,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }

@app.get("/")
async def root(): return get_payload()

@app.get("/audit/full")
async def audit(): return get_payload()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
