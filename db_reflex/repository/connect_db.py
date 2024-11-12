from sqlmodel import create_engine

def connect():
    engine = create_engine("sqlite:///reflex.db")
    return engine



