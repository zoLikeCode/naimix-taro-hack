from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, FLOAT, TEXT
from sqlalchemy.orm import relationship, deferred

from database import Base


class Resume(Base):
   __tablename__ = 'resumes'

   resume_id = Column(Integer, primary_key=True)
   url_to_resume = Column(String)
   download_date = Column(TIMESTAMP)