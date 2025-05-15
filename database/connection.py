from sqlalchemy import create_engine, text
from config_project import Const


engine = create_engine(url=Const.DATABASE_URL_psycopg())

with engine.connect() as conn:
    res = conn.execute(text("select version()"))
    print(f"{res.all()=}")