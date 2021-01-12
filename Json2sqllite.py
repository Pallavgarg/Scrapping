import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup
import pandas as pd
json_url = requests.get("https://github.com/nshntarora/Indian-Cities-JSON/blob/master/cities.json")
htmlContent = json_url.content
soup = BeautifulSoup(htmlContent, 'html.parser')
b=(soup.findAll("span",class_="pl-s"))
list = []
for i in b:
    s=(i.text)
    if s!='"name"' and s!='"id"' and s!='"state"':
        list.append(s[1:-1])

s=list
#for i in s[::3]:
    #print(i)

#for j in s[1::3]:
    #print(j)

#for k in s[2::3]:
    #print(k)

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    city_name text NOT NULL,                                    
                                    state text NOT NULL                                  
                                )"""

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def create_task(conn):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    for i in range(0, len(s), 3):
        sql = ''' INSERT OR IGNORE INTO tasks(id,city_name,state)
                  VALUES(?,?,?) '''
        task = (s[i],s[i+1],s[i+2])
        cur = conn.cursor()
        cur.execute(sql,task)
        conn.commit()
    return "done"


if __name__ == '__main__':
    conn = create_connection(r"C:\sqlite\pythonsqlite.db")
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_tasks_table)
        create_task(conn)
        db_df = pd.read_sql_query("SELECT * FROM tasks", conn)
        db_df.to_csv('database.csv', index=False)
