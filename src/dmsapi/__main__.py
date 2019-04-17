''' Trivial Eve-SQLAlchemy example. '''

from os import environ

from eve import Eve
from eve_swagger import swagger

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property

from eve_sqlalchemy import SQL
from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from eve_sqlalchemy.validation import ValidatorSQL

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(80))
    lastname = Column(String(120))
    fullname = column_property(firstname + " " + lastname)


SETTINGS = {
    'DEBUG': True,
    'SQLALCHEMY_DATABASE_URI': environ.get("DATABASE_URI", 'sqlite://'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    # api documentation
    'SWAGGER_INFO': {
        'title': 'DMS API',
        'version': '1.0',
        'description': 'an API description',
        'termsOfService': 'my terms of service',
        'contact': {
            'name': 'Dallas Makerspace',
            'url': 'http://dallasmakerspace.org'
        },
        'license': {
            'name': 'BSD',
            'url': 'https://github.com/Dallas-Makerspace/DMS-API/blob/master/LICENSE',
        },
        'schemes': ['http', 'https'],
    },
    'RENDERERS': ['eve.render.JSONRenderer'],
    'X_DOMAINS': "*",
    'X_HEADERS': "*",
    'X_ALLOW_CREDENTIALS': True,
    # backend schema
    'DOMAIN': DomainConfig({
        'people': ResourceConfig(People)
    }).render()
}


def main():
    app = Eve(auth=None, settings=SETTINGS, validator=ValidatorSQL, data=SQL)
    app.register_blueprint(swagger)
    
    # bind SQLAlchemy
    db = app.data.driver
    Base.metadata.bind = db.engine
    db.Model = Base
    db.create_all()


    # Insert some example data in the db
    if not db.session.query(People).count():

        db.session.add_all([
            People(firstname=u'George', lastname=u'Washington'),
            People(firstname=u'John', lastname=u'Adams'),
            People(firstname=u'Thomas', lastname=u'Jefferson')])
        db.session.commit()

    # using reloader will destroy in-memory sqlite db
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
