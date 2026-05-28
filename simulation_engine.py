from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class NodeModel(Base):
    __tablename__ = "nodes"
    id = Column(String, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)

class EdgeModel(Base):
    __tablename__ = "edges"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    source = Column(String, index=True)
    destination = Column(String, index=True)
    distance = Column(Float, nullable=False)

class TrafficHistoryModel(Base):
    __tablename__ = "traffic_history"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    edge_id = Column(Integer, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    value = Column(Float, nullable=False)
