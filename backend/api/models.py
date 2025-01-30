from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProjectData(Base):
    _tablename_ = "project_data"
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True)
    workers = Column(Integer)
    materials = Column(Integer)
    deadline_days = Column(Integer)