from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

Base = declarative_base()

class ToDoItem(Base):
    __tablename__ = "todoitems"
    item_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    done = Column(Boolean, nullable=False, default=False)