from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    project_id = Column(String, primary_key=True)
    project_name = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    status = Column(String, nullable=False)
    budget = Column(Float, nullable=False)


class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(String, primary_key=True)
    task_name = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    assigned_resource = Column(String, nullable=False)
    project_id = Column(String, ForeignKey("projects.project_id"))
    project = relationship("Project")

class Resource(Base):
    __tablename__ = "resources"
    resource_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    availability = Column(Integer, nullable=False)
    project_id = Column(String, ForeignKey("projects.project_id"))
    project = relationship("Project")

class OptimizedResourceAllocation(Base):
    __tablename__ = "optimized_resource_allocation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(String, ForeignKey("projects.project_id"), nullable=False)
    resource_id = Column(String, ForeignKey("resources.resource_id"), nullable=False)
    allocated_hours = Column(Float, nullable=False)
    efficiency_score = Column(Float, nullable=False)
    project = relationship("Project")
    resource = relationship("Resource")

class RiskAssessmentResults(Base):
    __tablename__ = "risk_assessment_results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(String, ForeignKey("projects.project_id"), nullable=False)
    risk_score = Column(Float, nullable=False)
    risk_factors = Column(String, nullable=False)
    project = relationship("Project")
