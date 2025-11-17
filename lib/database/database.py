from decouple import config
from sqlalchemy import create_engine

database_url = f"postgresql://{config("POSTGRES_USER")}:{config("POSTGRES_PWD")}@"
database_url += f"{config("POSTGRES_URL")}:{config("POSTGRES_PORT")}/{config("POSTGRES_DB")}"

engine = create_engine(database_url, echo=True)
"""Database engine, used to do requests"""