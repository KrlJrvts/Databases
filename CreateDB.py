import pymysql

db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    db=""
    )


with db.cursor() as c:
    c.execute("CREATE SCHEMA IF NOT EXISTS tallinnPensioners DEFAULT CHARACTER SET utf8")
    # c.execute("SELECT VERSION()")
    # version = c.fetchone()
    # print(f"Database version: {version[0]}")
db.close()


db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    db="tallinnPensioners"
    )
