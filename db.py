import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def fetch(self, acctask):
        self.cur.execute("SELECT *, oid FROM tasks where acctask=?", (acctask,))
        rows = self.cur.fetchall()
        return rows

    def insert(self, acctask, taskname, task):
        self.cur.execute("INSERT INTO tasks VALUES (?, ?, ?)",
                        (acctask, taskname, task))
        self.conn.commit()

    def remove(self, acctask):
        self.cur.execute("DELETE FROM tasks WHERE acctask=?",  (acctask))
        self.conn.commit()

    def update(self, acctask, taskname, task):
        self.cur.execute("UPDATE tasks SET taskname = ?, task = ? WHERE acctask = ? AND oid=?",
                        (acctask, taskname, task))
        self.conn.commit()

    def __del__(self):
        self.conn.close()