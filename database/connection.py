import psycopg2


class DBConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="123",
            port=5431,
            dbname="kadri_test"
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
