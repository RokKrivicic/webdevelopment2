from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("movie_database.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS Film_studio(
                id integer primary key autoincrement,
                name text);
                """)

db.execute("""CREATE TABLE IF NOT EXISTS Genre(
                id integer primary key autoincrement,
                name text);
                """)

db.execute("""CREATE TABLE IF NOT EXISTS Movie(
                id integer primary key autoincrement,
                name text,
                film_studio_id integer, 
                genre_id integer,
                movie_seen boolean,
                FOREIGN KEY(film_studio_id) REFERENCES Film_studio(id),
                FOREIGN KEY(genre_id) REFERENCES Genre(id));
                """)

db.execute("""CREATE TABLE IF NOT EXISTS Actor(
                id integer primary key autoincrement,
                name text,
                last_name text);
                """)

db.execute("""CREATE TABLE IF NOT EXISTS Director(
                id integer primary key autoincrement,
                name text,
                last_name text);
                """)

db.execute("""CREATE TABLE IF NOT EXISTS Movies_actors(
                id integer primary key autoincrement,
                movie_id integer,
                actor_id integer,
                FOREIGN KEY(movie_id) REFERENCES Movie(id),
                FOREIGN KEY(actor_id) REFERENCES Actor(id));
                """)

db.execute("""CREATE TABLE IF NOT EXISTS Movies_directors(
                id integer primary key autoincrement,
                movie_id integer,
                director_id integer,
                FOREIGN KEY(movie_id) REFERENCES Movie(id),
                FOREIGN KEY(director_id) REFERENCES Director(id));
                """)

db.print_tables(verbose=True)
