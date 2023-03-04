import pymysql
import datetime


def convert_line_to_values(line):
    values = line.split(",")
    # convert timestamp to datetime
    # values[0] = datetime.datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S")
    return values


if __name__ == "__main__":
    sql = """
        INSERT INTO sda 
        (id, first_name, last_name, sex, age, pen_amount, 
        nationality) VALUES
        (%s, %s, %s, %s, %s, %s, %s)
    """

    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        db="tallinnPensioners"
    )

    with db.cursor() as c:
        with open("talllinn_pensioners.csv") as f:
            for i, line in enumerate(f):
                if i == 0:  # skip column names
                    continue
                values = convert_line_to_values(line)
                c.execute(sql, values)
                if i > 0 and i % 100 == 0:
                    db.commit()
        db.commit()
    db.close()
