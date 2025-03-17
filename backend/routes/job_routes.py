from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.models import Job

router = APIRouter()

# Get all jobs
@router.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

# Add a new job
@router.post("/jobs")
def create_job(title: str, company: str, location: str, salary: float, description: str, url: str, db: Session = Depends(get_db)):
    new_job = Job(title=title, company=company, location=location, salary=salary, description=description, url=url)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job
