import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

from database import engine, Base
from routers import users, appointments, messages # Add other routers as needed

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Healthcare Patient Portal", version="1.0.0", openapi_url="/openapi.json", docs_url="/docs")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # Replace with your allowed origins in production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Router Registration
app.include_router(users.router)
app.include_router(appointments.router)
app.include_router(messages.router) # Add other routers here

# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Static File Serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
    @app.get("/{file_path:path}")
    async def serve_frontend(file_path: str, request: Request):
        if file_path.startswith("api"):
            return await request.app.dispatch(request)
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")

# Exception Handling
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
