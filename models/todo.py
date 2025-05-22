from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    items = relationship("Item", backref="todo", cascade="all, delete")