import psycopg2

from config_project import Const


class DBConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=Const.DB_HOST,
            user=Const.DB_USER,
            password=Const.DB_PASSWORD,
            port=Const.DB_PORT,
            dbname=Const.DB_NAME
        )
        print("подключено")
        self.cursor = self.conn.cursor()

    def test(self):
        self.cursor.execute("delete from subfed")
        self.cursor.execute("select * from subfed")
        print(self.cursor.fetchall())
        with open("CSVs/default/SubFed.csv", "r", encoding="utf-8") as f:
            self.cursor.copy_expert("COPY subfed (id, name) FROM STDIN WITH CSV HEADER DELIMITER ';'", f)
        self.cursor.execute("select * from subfed")
        print(self.cursor.fetchall())
        self.conn.commit()
