from sqlalchemy import Column, Integer, String, SmallInteger, Text, ForeignKey, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'Company'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    safe_name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    telephone = Column(Integer, nullable=False)
    enterprise = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated = Column(DateTime(timezone=True), nullable=False, default=func.now())
