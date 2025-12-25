from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
DATABASE_URL = "postgresql://url_shortener_db_rmo3_user:wqutYMBbxeNxrtIz8WwrssCaQ8hppHWx@dpg-d569bk3uibrs739fucb0-a/url_shortener_db_rmo3"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
