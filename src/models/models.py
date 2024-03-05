from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base


BASE = declarative_base()

class Candidates(BASE):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    application_date = Column(Date, nullable=False)
    country = Column(String(100), nullable=False)
    yoe = Column(Integer, nullable=False)
    seniority = Column(String(100), nullable=False)
    technology = Column(String(100), nullable=False)
    code_challenge_score = Column(Integer, nullable=False)
    technical_interview_score = Column(Integer, nullable=False)


class HiredCandidate(BASE):
    __tablename__ = 'hired_candidates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    application_date = Column(Date, nullable=False)
    country = Column(String(100), nullable=False)
    yoe = Column(Integer, nullable=False)
    seniority = Column(String(100), nullable=False)
    technology = Column(String(100), nullable=False)
    code_challenge_score = Column(Integer, nullable=False)
    technical_interview_score = Column(Integer, nullable=False)
    category_of_technology = Column(String(100), nullable=True)
    hired = Column(Integer, nullable=True)


