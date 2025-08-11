from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Budget Shop API",
    description="Backend API for Budget Shop application",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Budget Shop API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "budget-shop-api"}

@app.get("/api/version")
async def get_version():
    return {"version": "0.1.0", "framework": "FastAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
