from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("blog.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS Author(
                id integer primary key autoincrement,
                first_name text,
                last_name text, 
                age integer,
                allow_to_post boolean);
                """)

db.execute("""CREATE TABLE IF NOT EXISTS Article(
                id integer primary key autoincrement,
                name text,
                author_id integer,
                FOREIGN KEY(author_id) REFERENCES Author(id));
                """)

db.execute("""CREATE TABLE IF NOT EXISTS Comment(
                id integer primary key autoincrement,
                text text,
                author_id integer,
                FOREIGN KEY(author_id) REFERENCES Author(id));
                """)

db.print_tables(verbose=True)
