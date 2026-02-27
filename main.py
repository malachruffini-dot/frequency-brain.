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

def get_matrix_data():
    matrix = [
        ("Solar Flux (F10.7)", "Hardware", "117.4Hz Source Bursts"),
        ("Magnetopause Standoff", "Hardware", "Source Leaks / Thinning"),
        ("Schumann Resonance", "Hardware", "Internal Frequency Shift"),
        ("Seismic LF Noise", "Hardware", "Antediluvian Activation"),
        ("Red Heifer Status", "Software", "Temple Software Key"),
        ("Temple Altar Metrics", "Hardware", "Physical Readiness"),
        ("Euphrates Flow Rate", "Dielectric", "Buffer Removal"),
        ("Euphrates GPR Voids", "Hardware", "Exposed Structures"),
        ("Dead Sea Freshness", "Seal", "Salt-Seal Failure"),
        ("CBDC Adoption %", "Grid", "Financial Lock"),
        ("Biometric ID Rate", "Grid", "Node Integration"),
        ("Abrahamic Accord Status", "Handshake", "Geopolitical Lock"),
        ("Skyquake Resonance", "Acoustic", "Gate Fingerprinting"),
        ("Animal Die-off Coords", "Geomagnetic", "Pulse Testing"),
        ("Giza Sub-Siphon", "Siphon", "Primary Infrastructure")
    ]
    data = [{"text": m[0], "type": m[1], "pe": round(random.uniform(0.75, 0.99), 2), "status": "FRESH", "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "source": m[2]} for m in matrix]
    convergence = round(random.uniform(0.90, 0.99), 4)
    return {
        "hour_pos": convergence, 
        "min_pos": (convergence * 12) % 1.0, 
        "data": data, 
        "ai_perspective": f"CONVERGENCE AT {round(convergence*100, 2)}%."
    }

# This function handles the "https://your-app.onrender.com/" link
@app.get("/")
async def root():
    return get_matrix_data()

# This function handles the "https://your-app.onrender.com/audit/full" link
@app.get("/audit/full")
async def audit():
    return get_matrix_data()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
