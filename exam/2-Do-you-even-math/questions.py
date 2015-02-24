from sqlalchemy import Column, Integer, String
from connection import *


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(Integer)

    def __str__(self):
        return "{}".format(self.question)

    def __repr__(self):
        return self.__str__()
