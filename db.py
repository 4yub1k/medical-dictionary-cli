import sqlite3


class Database:
    def __init__(self, db_file) -> None:
        self.con = sqlite3.connect(f"{db_file}.db")
        self.cur = self.con.cursor()

    def create_table(self, **kwrds):
        # Avoid f strings in raw quiries.
        table_name = kwrds["table_name"]
        del kwrds["table_name"]
        kwrds.update({"word": f"{kwrds["word"]} string primary key"})
        columns = ",".join(kwrds.values())

        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({columns})")
        # self.con.commit()

    def drop_table(self, name=None):
        self.cur.execute(f"DROP TABLE {name}")

    def insert_value(self, data=None):
        try:
            self.cur.executemany("INSERT INTO dictionary VALUES(?, ?)", data)
        except sqlite3.IntegrityError as ie:
            # print("Already exists in Table:", ie)
            print("\nWord already exists in Database")
        except TypeError:
            print("\nNot Found in db/files")
        self.con.commit()
        self.con.close()

    def search_table(self, word):
        self.cur.execute(f"SELECT * FROM dictionary WHERE Word LIKE '{word}%'")
        rows = self.cur.fetchall()
        self.con.close()
        return rows


if __name__ == "__main__":
    db_dict = Database("dictionary")
    # db_dict.drop_table("dictionary111")
    db_dict.create_table(table_name="dictionary", word="Word", meaning="Meaning")
