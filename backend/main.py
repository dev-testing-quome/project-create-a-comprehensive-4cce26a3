import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from sqlalchemy.orm import Session

from backend.database import SessionLocal, engine
from backend.routers import users, appointments, messages, medical_records, prescriptions, billing
from backend.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Replace with your allowed origins in production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routers
app.include_router(users.router)
app.include_router(appointments.router)
app.include_router(messages.router)
app.include_router(medical_records.router)
app.include_router(prescriptions.router)
app.include_router(billing.router)

# Health check
@app.get('/health')
def health_check():
    return {'status': 'ok'}

# Static Files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{{"file_path:path}}")
    async def serve_frontend(file_path: str):
        if file_path.startswith("api/") or file_path == "":
            return None  # Let API routes handle it
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")

#Exception Handling
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# Start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
