# imports
import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
    #Shows accounts tasks that you are logged in
    def fetch(self, acctask):
        self.cur.execute("SELECT *, oid FROM tasks where acctask=?", (acctask,))
        rows = self.cur.fetchall()
        return rows
    # Add's new task
    def insert(self, acctask, taskname, task):
        self.cur.execute("INSERT INTO tasks VALUES (?, ?, ?)",
                        (acctask, taskname, task))
        self.conn.commit()

    # Delete's selected Task 
    def remove(self, TaskSelect):
        self.cur.execute("DELETE FROM tasks WHERE taskname=?",  (TaskSelect,))
        self.conn.commit()
    # Update's selected task
    def update(self, TaskSelect, taskname, task):
        self.cur.execute("UPDATE tasks SET taskname = ?, task = ? WHERE taskname = ?",
                        (taskname, task, TaskSelect))
        self.conn.commit()

    def __del__(self):
        self.conn.close()