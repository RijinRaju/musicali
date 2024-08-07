import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv('.env')

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')



SQLALCHEMY_DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal = sessionmaker(bind= engine)

Base = declarative_base()

# to end the session
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()