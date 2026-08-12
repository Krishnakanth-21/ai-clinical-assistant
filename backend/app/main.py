from fastapi import FastAPI

app = FastAPI(
    title="AI Clinical Assistant API",
    version="1.0.0",
    description="Backend API for AI Clinical Assistant"
)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Clinical Assistant",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "message": "Application is running successfully"
    }
