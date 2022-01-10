import psycopg2

# connect tom the db
con = psycopg2.connect(host = 'localhost',database = 'test',user = 'postgres',password = 'password', port = 5432)

#cursor
cur = con.cursor()

# execute the code
cur.execute(
    """CREATE TABLE hotel (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    ratings VARCHAR(50),
    location VARCHAR(50) NOT NULL,
    price VARCHAR(50) NOT NULL,
    imagelink VARCHAR(100),
    amenities VARCHAR(50) 
)""")


# rows = cur.fetchall()

# for r in rows:
#     print(f"id => {r[0]} title => {r[1]} ratings => {r[2]}")

# close the cursor
cur.close()

# close the connection
con.close()
