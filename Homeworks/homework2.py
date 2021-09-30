from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.pretty_print("SELECT * FROM Invoice WHERE Total = (SELECT MAX(Total) FROM Invoice);")  # Most expensive order

db.pretty_print("SELECT * FROM Invoice WHERE Total = (SELECT MIN(Total) FROM Invoice);")  # Cheapest orders

db.pretty_print('SELECT BillingCity, COUNT(InvoiceId) AS NumberOfOrders FROM Invoice GROUP BY BillingCity ORDER BY '
                'NumberOfOrders DESC limit 1;')  # City with the most orders

db.pretty_print("""SElECT COUNT(Track.TrackId) AS NumberOfProtectedAACAudioFiles
                    FROM Track
                    LEFT JOIN MediaType ON MediaType.MediaTypeId = Track.MediaTypeId
                    WHERE MediaType.Name = 'Protected AAC audio file'
                    """)  # Number of tracks with MediaType Protected AAC audio file

db.pretty_print("""SELECT Artist.Name, COUNT(Album.AlbumId) AS NUmberOfAlbums
                    FROM ALBUM
                    LEFT JOIN Artist ON Artist.ArtistId = Album.ArtistId
                    GROUP BY Artist.Id
                    ORDER BY NumberOfAlbums DESC LIMIT 1
                    """)  # Artist with the most albums

db.pretty_print("""SELECT Genre.Name, COUNT(Track.TrackId) AS NUmberOfTracks
                    FROM Track
                    LEFT JOIN Genre ON Genre.GenreId = Track.GenreId
                    GROUP BY Genre.Id
                    ORDER BY NUmberOfTracks DESC LIMIT 1
                    """)  # Genre with the most tracks

db.pretty_print("""SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS MoneySpent
                    FROM Invoice
                    LEFT JOIN Customer ON Customer.CustomerId = Invoice.CustomerId
                    GROUP BY Customer.FirstName, Customer.LastName
                    ORDER BY MoneySpent DESC LIMIT 1
                    """)  # Customer with most money spent

db.pretty_print("""SELECT Track.Name, Invoice.InvoiceId 
                    FROM InvoiceLine
                    LEFT JOIN Track ON Track.TrackId = InvoiceLine.TrackId
                    LEFT JOIN Invoice ON Invoice.InvoiceId = InvoiceLine.InvoiceId
                    """)  # Songs per order
