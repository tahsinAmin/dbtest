import psycopg2

# https://www.youtube.com/watch?v=M2NzvnfS-hI

# connect tom the db
conn = None
cur = None
try:
    print("start")
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'test',
        user = 'postgres',
        password = 'password',
        port = 5432)

    #cursor
    cur = conn.cursor()

    # execute the code
    create_script = """CREATE TABLE IF NOT EXISTS employee (
                        id      int NOT NULL PRIMARY KEY,
                        name    VARCHAR(40) NOT NULL,
                        salary  int,
                        dept_id VARCHAR(30))"""
    cur.execute(create_script)

    # drop_script = """DROP TABLE employee"""
    # cur.execute(drop_script)

    # save any transactions that we have done in the database
    conn.commit()

except Exception as error:
    print(error)
finally:
    # finally will execute with or wiothout any error bcz if and error occurs, the try block stops.    
    
    if cur is not None:   
        # close the cursor
        cur.close()

    if conn is not None: 
        # close the connection
        conn.close()
