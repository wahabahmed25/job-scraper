from sqlalchemy import Column, Integer, String, Text, DECIMAL, TIMESTAMP
from ..database import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    company = Column(String(255))
    location = Column(String(255))
    salary = Column(DECIMAL(10,2))
    description = Column(Text)
    url = Column(Text)
    scraped_at = Column(TIMESTAMP, default=datetime.utcnow)
