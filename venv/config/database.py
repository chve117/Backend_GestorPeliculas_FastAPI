import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
"""Se guarda nombre de base de datos"""
sqlite_file_name = "../database.sqlite"
"""Se lee el directorio actual del archivo database"""
base_dir = os.path.dirname(os.path.realpath(__file__))
"""Es la forma en la que se conecta una base de datos, se una la url"""
database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"
engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()