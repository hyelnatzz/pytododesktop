from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime


Base = declarative_base()


#database clase
class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __repr__(self) -> str:
        return f'<Task "{self.title}"">'

