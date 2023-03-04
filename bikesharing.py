import pymysql


create_sql = """
CREATE TABLE IF NOT EXISTS `bikesharing` (
    `tstamp` timestamp,
    `cnt` integer,
    `temperature` decimal(5, 2),
    `temperature_feels` decimal(5, 2),
    `humidity` decimal(4, 1),
    `wind_speed` decimal(5,2),
    `weather_code` integer,
    `is_holiday` boolean,
    `is_weekend` boolean,
    `season` integer
);
"""


db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    db="default1"
    )


with db.cursor() as c:
    c.execute(create_sql)
    c.execute("SELECT count(*) FROM `bikesharing`;")
    result = c.fetchall()
    if result and result[0] == 0:
        print("Successfully created bikesharing table!")
db.close()
