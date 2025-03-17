from sqlalchemy.orm import Session
from .database import SessionLocal
from .models.models import Job

# Fake data
jobs = [
    {"title": "Software Engineer", "company": "Google", "location": "California", "salary": 120000.00, "description": "Develop and scale web apps", "url": "https://google.com"},
    {"title": "Data Scientist", "company": "Meta", "location": "New York", "salary": 110000.00, "description": "Analyze big data", "url": "https://meta.com"},
    {"title": "Product Manager", "company": "Amazon", "location": "Seattle", "salary": 130000.00, "description": "Manage product lifecycle", "url": "https://amazon.com"},
]

# Connect to DB session
db: Session = SessionLocal()

# Add each job to DB
for job_data in jobs:
    job = Job(**job_data)
    db.add(job)

# Commit to save changes
db.commit()
db.close()
