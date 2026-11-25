from fastapi import FastAPI

app = FastAPI(title="Agro Guide API", version="0.1.0")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "agro-guide-api"}
