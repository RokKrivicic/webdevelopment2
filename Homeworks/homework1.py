from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

# all tables in the database
db.print_tables(verbose=True)

#This database has many tables. Write an SQL command that will print Name
# from the table Artist (for all the database entries)
db.pretty_print("SELECT Name FROM Artist;")

#Print all data from the table Invoice where BillingCountry is Germany
db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany';")

#Count how many albums are in the database. Look into the SQL documentation for help.
# Hint: look for Min&Max and Count, Avg, Sum
db.pretty_print("SELECT COUNT(AlbumId) AS 'Number of albums' FROM Album;")

#How many customers are from France?
db.pretty_print("SELECT COUNT(CustomerId) AS 'Number of costumer from France' FROM Customer WHERE Country = 'France';")