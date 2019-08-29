import sqlite3



def connect():
    conn=sqlite3.connect("movies.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY,title text, genre text, year integer, runtime text)")
    conn.commit()
    conn.close()

def insert(title,genre,year,runtime):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movie VALUES (NULL,?,?,?,?)", (title,genre,year,runtime))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("movies.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM movie")
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="",genre="",year="",runtime=""):
    conn=sqlite3.connect("movies.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM movie WHERE title=? OR genre=? OR year=? OR runtime=?",(title,genre,year,runtime))
    rows=cursor.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM movie WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,genre,year,runtime):
    conn=sqlite3.connect("movies.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE movie SET title=?,genre=?,year=?,runtime=? WHERE id=?",(title,genre,year,runtime,id))
    conn.commit()
    conn.close()


#print(type(search("","","","")))
#print(search("Avatar22"))
#insert("rff","frr",55,"rrr")
#print(view())
connect()