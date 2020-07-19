import sqlite3
import os
import json

class DBManager:
    def __init__(self, db_filename):
        print(db_filename)
        self.db_file = db_filename
        isExistDB = os.path.exists(self.db_file)
        self.create_db_connection()
        if not isExistDB:
            self.create_db_table()

    def create_db_connection(self):
        self.db_conn = None
        try:
            self.db_conn = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(e)

    def create_db_table(self):
        print("create_table")
        create_memno_table_sql = '''CREATE TABLE IF NOT EXISTS minim (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        memo text
                                    );'''
        try:
            c = self.db_conn.cursor()
            c.execute(create_memno_table_sql)
        except sqlite3.Error as e:
            print(e)

    def insert(self, data):
        intert_memno_sql = '''INSERT INTO minim(title, memo) VALUES(?, ?);'''
        print(data)
        try:
            cur = self.db_conn.cursor()
            cur.execute(intert_memno_sql, (data[0], data[1]))
            self.db_conn.commit()
            print(cur.lastrowid)
            return cur.lastrowid
        except sqlite3.Error as e:
            print(e)
        return -1

    def update(self, data):
        update_memno_sql = '''UPDATE minim SET title=?, memo=? WHERE id=?;'''
        try:
            cur = self.db_conn.cursor()
            cur.execute(update_memno_sql, (data[0], data[1], data[2]))
            self.db_conn.commit()
        except sqlite3.Error as e:
            print(e)

    def delete(self, index):
        update_memno_sql = '''DELETE FROM minim WHERE id=?;'''
        try:
            cur = self.db_conn.cursor()
            cur.execute(update_memno_sql, (index,))
            self.db_conn.commit()
        except sqlite3.Error as e:
            print(e)

    def load(self):
        print("Load DB")
        rows = []
        try:
            cur = self.db_conn.cursor()
            cur.execute("SELECT * FROM minim")

            rows = cur.fetchall()
        except sqlite3.Error as e:
            print(e)
        return self.processData(rows)

    def processData(self, data):
        memoList = {}

        for memo in data:
            item = {}
            item['index'] = str(memo[0])
            item['id'] = memo[1]
            item['memo'] = json.loads(memo[2])
            memoList[item['index']] = item

        return memoList

    def printDB(self):
        rows = self.load()
        for k, row in rows.items():
            print(row)

def main():
    pass

if __name__ == '__main__':
    main()