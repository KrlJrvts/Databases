import pymysql
import datetime


db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    db="default1"
    )

with db.cursor() as c:
    c.execute(
        "SELECT tstamp,cnt FROM bikesharing WHERE tstamp BETWEEN %s AND %s",
        (datetime.datetime(2016, 1, 1, 0), datetime.datetime(2016, 1, 1, 5)),
    )
    print(f"Column names: {[d[0] for d in c.description]}")
    print(c.fetchone())  # first row
    print(c.fetchmany(4))
    print(c.fetchall())  # remaining rows
    print(f"Got {c.rowcount} rows")

db.close()