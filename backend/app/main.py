from fastapi import FastAPI

app = FastAPI(title="Grad Funding API")

@app.get("/")
def root():
    return {"status": "ok"}
