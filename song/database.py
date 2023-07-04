import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("main_db")
        self.cur = self.conn.cursor()
        self.conn.execute('CREATE TABLE IF NOT EXISTS main_table(id integer PRIMARY KEY AUTOINCREMENT, borough text, vacation_spot text, latitude float, longitude float, location_address text, call_address text, homepage text, day_off text, work_time text, convenience text )')


