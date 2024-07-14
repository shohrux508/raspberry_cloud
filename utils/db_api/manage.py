from data.database import *
import datetime


def create_id(table, id_index):
    cur.execute(f"""SELECT * FROM {table}""")
    result = cur.fetchall()
    id_index = int(id_index)
    if result == []:
        id = 1
    else:
        id = result[-1][id_index] + 1
    return id


class LED():
    def new(self, color):
        time = datetime.datetime.now("")
        cur.execute(f'''INSERT INTO led VALUES("{id}", "{color}", "0", "{time}")''')
    def turn(self, pin, status=1):
        cur.execute(f'''UPDATE led SET status = {status} WHERE pin = {pin}''')
        conn.commit()
        return True
    def get(self, pin):
        cur.execute(f'''SELECT * FROM led WHERE pin = {pin}''')
        led = cur.fetchone()
        return led
        