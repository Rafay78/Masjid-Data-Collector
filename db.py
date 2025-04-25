from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import settings

# RDS_AURORA_URL = f"postgresql://{settings.username}:{settings.password}@rds-aurora-aurora-instance.cgliiwu4obpq.us-east-1.rds.amazonaws.com:5432/mydatabase"
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.username}:{settings.password}@localhost:15432/mydatabase"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    # RDS_AURORA_URL
    # , connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close