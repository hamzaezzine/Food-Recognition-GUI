import sqlite3

class Database:
    def __init__(self,db): 
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS users(
            id Integer Primary Key,
            firstname text,
            lastname text,
            email text,
            password text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self,firstname,lastname,email,password):
        self.cur.execute("insert into users values(NULL,?,?,?,?)",
                        (firstname,lastname,email,password))
        self.con.commit()

    def get_users(self):
        self.cur.execute("SELECT * FROM users") 
        rows = self.cur.fetchall()
        return rows
    
    def get_user(self, email):
        self.cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = self.cur.fetchone()
        if row:
            return [row]  
        else:
            return None
        
    def get_user_by_id(self, id):
        self.cur.execute("SELECT * FROM users WHERE id = ?", (id,))
        row = self.cur.fetchone()
        if row:
            return [row]  
        else:
            return None

    def update_user(self, firstname, lastname, email, id):
        self.cur.execute('UPDATE users SET firstname = ?, lastname = ?, email = ? WHERE id = ?',(firstname,lastname, email, id))
        self.con.commit()

    def update_pass(self, password, id):
        self.cur.execute('UPDATE users SET password = ? WHERE id = ?',(password, id))
        self.con.commit()

    def remove_user(self, email):
        self.cur.execute("DELETE FROM users WHERE email = ?",(email))
        self.con.commit()