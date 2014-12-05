from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    HTML_version = Column(String)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.url, self.title, self.HTML_version)

    def __repr__(self):
        return self.__str__()


class pages(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    website = Column(String)
    url = Column(String)
    title = Column(String)
    description = Column(String)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.website, self.url, self.title, self.description)

    def __repr__(self):
        return self.__str__()


engine = create_engine("sqlite:///search_engine.db")
# will create all tables
Base.metadata.create_all(engine)


class fnctions:

    def __init__(self):
        self.session = Session(bind=engine)

    def add_website(self, myUrl, myTitle, myHTML_version):
        web = website(url=myUrl, title=myTitle, HTML_version=myHTML_version)
        self.session.add(web)
        self.session.commit()

    def add_page(self, myWebsite, myUrl, myTitle, myDescription):
        page = pages(website=myWebsite, url=myUrl, title=myTitle, description=myDescription)
        self.session.add(page)
        self.session.commit()

    def select_everything(self, from_table):
        result = self.session.query(from_table).all()
        return result


a = fnctions()
a.add_website("ala2", "title2", "HTML5")
a.add_page("haha.com", "ala2", "title2", "description")
print(a.select_everything(pages))
