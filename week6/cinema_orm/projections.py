# projections.py

from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
#from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
#from sqlalchemy.orm import relationship
from movies import *

Base = declarative_base()

engine = create_engine("sqlite:///cinema.db")

session = Session(bind=engine)

#session.add_all([Movies(name='The Hunger Games: Catching Fire', rating=7.9),
#                 Movies(name='Wreck-It Ralph', rating=7.8),
#                 Movies(name='Her', rating=8.3)])
#session.commit()
#
#session.add_all([Projections(movie_id=1, type='3D', date='2014-04-01', time='19:10', seats=100),
#                 Projections(movie_id=1, type='2D', date='2014-04-01', time='19:00', seats=100),
#                 Projections(movie_id=1, type='4DX', date='2014-04-02', time='21:00', seats=100),
#                 Projections(movie_id=3, type='2D', date='2014-04-05', time='20:20', seats=100),
#                 Projections(movie_id=2, type='3D', date='2014-04-02', time='22:00', seats=100),
#                 Projections(movie_id=2, type='2D', date='2014-04-02', time='19:30', seats=100)])
#session.commit()
#
#session.add_all([Reservations(username='RadoRado', projection_id=1, row=2, col=1),
#                 Reservations(username='RadoRado', projection_id=1, row=3, col=5),
#                 Reservations(username='RadoRado', projection_id=1, row=7, col=8),
#                 Reservations(username='Ivo', projection_id=3, row=1, col=1),
#                 Reservations(username='Ivo', projection_id=3, row=1, col=2),
#                 Reservations(username='Mysterious', projection_id=5, row=2, col=3),
#                 Reservations(username='Mysterious', projection_id=5, row=2, col=4)])
#
#session.commit()


class Cinema:

    def __init__(self):
        self.Base = declarative_base()
        self.engine = create_engine("sqlite:///cinema.db")
        self.session = Session(bind=engine)

    def initialisation(self):
        self.session.add_all([Movies(name='The Hunger Games: Catching Fire', rating=7.9),
                              Movies(name='Wreck-It Ralph', rating=7.8),
                              Movies(name='Her', rating=8.3)])
        self.session.commit()

        self.session.add_all([Projections(movie_id=1, type='3D', date='2014-04-01', time='19:10', seats=100),
                              Projections(movie_id=1, type='2D', date='2014-04-01', time='19:00', seats=100),
                              Projections(movie_id=1, type='4DX', date='2014-04-02', time='21:00', seats=100),
                              Projections(movie_id=3, type='2D', date='2014-04-05', time='20:20', seats=100),
                              Projections(movie_id=2, type='3D', date='2014-04-02', time='22:00', seats=100),
                              Projections(movie_id=2, type='2D', date='2014-04-02', time='19:30', seats=100)])
        self.session.commit()

        self.session.add_all([Reservations(username='RadoRado', projection_id=1, row=2, col=1),
                              Reservations(username='RadoRado', projection_id=1, row=3, col=5),
                              Reservations(username='RadoRado', projection_id=1, row=7, col=8),
                              Reservations(username='Ivo', projection_id=3, row=1, col=1),
                              Reservations(username='Ivo', projection_id=3, row=1, col=2),
                              Reservations(username='Mysterious', projection_id=5, row=2, col=3),
                              Reservations(username='Mysterious', projection_id=5, row=2, col=4)])

        self.session.commit()

    def show_movies(self):

        all_movies = session.query(Movies).order_by(Movies.rating).all()
        print(all_movies)

x = Cinema()
x.initialisation()
x.show_movies()
