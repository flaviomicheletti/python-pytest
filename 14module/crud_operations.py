import sqlite3

# create connection to the database
conn = sqlite3.connect("module14.db")
c = conn.cursor()

# create a table to store data
c.execute(
    """CREATE TABLE IF NOT EXISTS example_table
             (id INTEGER PRIMARY KEY, name text, age integer)"""
)

# function to create a new record in the database
def create_record(conn, name, age):
    conn.execute("INSERT INTO example_table (name, age) VALUES (?, ?)", (name, age))
    conn.commit()


# function to read all records from the database
def read_records(conn):
    conn.execute("SELECT * FROM example_table")
    return c.fetchall()


# function to update a record in the database
def update_record(conn, id, name, age):
    conn.execute("UPDATE example_table SET name=?, age=? WHERE id=?", (name, age, id))
    conn.commit()


# function to delete a record from the database
def delete_record(conn, id):
    conn.execute("DELETE FROM example_table WHERE id=?", (id,))
    conn.commit()


# close the database connection when we're done
# conn.close()
