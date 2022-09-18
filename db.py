from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

DB_CONNECTION = 'sqlite:///db\scada.db?check_same_thread=False'
engine = create_engine(DB_CONNECTION,echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)