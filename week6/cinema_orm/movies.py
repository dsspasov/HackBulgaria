# movies.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
#from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

Base = declarative_base()

engine = create_engine("sqlite:///cinema.db")


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    def __str__(self):
        return "{} - {} - {}".format(self.id, self.name, self.rating)

    def __repr__(self):
        return self.__str__()


class Projections(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    type = Column(String)
    date = Column(String)
    time = Column(String)
    seats = Column(Integer, default=0)
    Movies = relationship("Movies", backref="projections")


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("projections.id"))
    row = Column(Integer)
    col = Column(Integer)
    Projections = relationship("Projections", backref="reservations")


# will create all tables
Base.metadata.create_all(engine)
