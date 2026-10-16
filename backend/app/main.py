from fastapi import FastAPI

app = FastAPI(
    title="MindMetrics AI",
    description="AI-powered mental wellbeing score prediction API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to MindMetrics AI",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "mindmetrics-api",
    }