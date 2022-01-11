import psycopg2
import psycopg2.extras

# change password when in office
# https://www.youtube.com/watch?v=M2NzvnfS-hI

# connect tom the db
conn = None

# for office
# try:
# with psycopg2.connect(
#     host = 'localhost',
#     database = 'test',
#     user = 'postgres',
#     password = 'password',
#     port = 5432) as conn


try:
    # for home
    with psycopg2.connect(
            host='localhost',
            database='db',
            user='postgres',
            password='root',
            port=5432) as conn:

        # cursor
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            # Drop table if exist before starting insertion. this is because we donn't want error for duplicate keys.
            drop_script = """DROP TABLE employee"""
            cur.execute(drop_script)

            # execute the code
            create_script = """CREATE TABLE IF NOT EXISTS employee (
                                id      int NOT NULL PRIMARY KEY,
                                name    VARCHAR(40) NOT NULL,
                                salary  int,
                                dept_id VARCHAR(30))"""
            cur.execute(create_script)

            insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'James', 1200, 'D1'),
                             (2, 'Robin', 1300, 'D1'),
                             (3, 'Xavier', 1400, 'D1')]
            for record in insert_values:
                cur.execute(insert_script, record)

            update_script = 'UPDATE employee SET salary = salary + (salary *0.5);'
            cur.execute(update_script)

            delete_record = ('James',)
            delete_script = 'DELETE FROM employee WHERE name = %s'
            cur.execute(delete_script, delete_record)

            print("Name | Salary")
            print("-----+-------")
            cur.execute('SELECT * FROM employee')
            for record in cur.fetchall():
                print(record['name'], record['salary'])


except Exception as error:
    print(error)
finally:
    # finally will execute with or wiothout any error bcz if and error occurs, the try block stops.

    if conn is not None:
        # close the connection
        conn.close()
