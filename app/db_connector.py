from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import config


engine = create_engine(config['testing'].TEST_DATABASE_URL)
engine.connect()
Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)


