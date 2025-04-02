import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="123",
    port=5431,
    dbname="kadri_test"
)

if conn:
    print("подключено")

cursor = conn.cursor()

with open("/CSVs/default/SubFed.csv", 'r', encoding='utf-8') as f:
    cursor.copy_expert("COPY subfed (id, name) FROM STDIN WITH CSV HEADER DELIMITER ';'", f)

cursor.execute("select * from subfed")
conn.commit()
result = cursor.fetchall()
print(result)