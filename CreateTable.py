import pymysql


create_sql = """
CREATE TABLE IF NOT EXISTS `sda` (
    `id` integer,
    `first_name` varchar(100),
    `last_name` varchar(100),
    `sex` varchar(7),
    `age` integer(3),
    `pen_amount` integer,
    `nationality` varchar(10)
);
"""


db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    db="tallinnPensioners"
    )


with db.cursor() as c:
    c.execute(create_sql)
    c.execute("SELECT count(*) FROM `sda`;")
    result = c.fetchall()
    if result and result[0] == 0:
        print("Successfully created sda table!")
db.close()
