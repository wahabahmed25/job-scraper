from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
#import the routes
from .routes.job_routes import router as job_router

app = FastAPI()

# Allow frontend (React) to talk to backend (FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#runs when server starts
@app.on_event("startup")
async def startup_event():
    print("backend running...")

#register job routes
app.include_router(job_router)
