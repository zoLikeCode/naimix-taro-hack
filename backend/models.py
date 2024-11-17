from sqlalchemy import Column,  Integer, ForeignKey, String, TIMESTAMP, TEXT, DOUBLE_PRECISION
from sqlalchemy.orm import relationship, deferred

from database import Base


class Resume(Base):
   __tablename__ = 'resumes'

   resume_id = Column(Integer, primary_key=True)
   url_to_resume = Column(String)
   download_date = Column(TIMESTAMP)

class UserProfile(Base):
   __tablename__ = 'user_profile'

   user_profile_id = Column(Integer, primary_key=True)
   full_name = Column(String)
   birthday = Column(String)
   prof = Column(String)
   phone_number = Column(String)
   experience = Column(String)
   summary_by_taro = Column(TEXT)
   recomendation = Column(TEXT)
   salary = Column(String)
   email = Column(String)
   city = Column(String)
   education = Column(String)
   faculty = Column(String)
   summary_by_resume = Column(TEXT)
   job_experience = Column(TEXT)
   about = Column(TEXT)
   url_photo = Column(String)
   resume_id = deferred(Column(Integer, ForeignKey(Resume.resume_id)))

   resume = relationship('Resume', foreign_keys='UserProfile.resume_id')

class UserTaro(Base):
   __tablename__ = 'user_with_taro'

   taro_id = Column(Integer, primary_key=True)
   user_profile_id = deferred(Column(Integer, ForeignKey(UserProfile.user_profile_id)))
   taro_info = Column(TEXT)
   cards = Column(String)
   status = Column(String)

   user_profile = relationship('UserProfile', foreign_keys='UserTaro.user_profile_id')

class Metrics(Base):
   __tablename__ = 'metrics'

   metric_id = Column(Integer, primary_key=True)
   stress_resistance = Column(DOUBLE_PRECISION)
   flexibility = Column(DOUBLE_PRECISION)
   communication_skills = Column(DOUBLE_PRECISION)
   creativity = Column(DOUBLE_PRECISION)
   initiative = Column(DOUBLE_PRECISION)
   leadership_qualities = Column(DOUBLE_PRECISION)
   professional_competence = Column(DOUBLE_PRECISION)
   ability_decisions = Column(DOUBLE_PRECISION)
   hard_work = Column(DOUBLE_PRECISION)
   organizational_skills = Column(DOUBLE_PRECISION)
   productivity = Column(DOUBLE_PRECISION)
   teamwork = Column(DOUBLE_PRECISION)
   taro_id = deferred(Column(Integer, ForeignKey(UserTaro.taro_id)))

   user_taro = relationship('UserTaro', foreign_keys='Metrics.taro_id')