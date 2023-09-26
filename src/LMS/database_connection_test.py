import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(database="lms", 
                        user="postgres",
                        password="pun123$sA", 
                        host="172.29.208.1", port="5432")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM details")

# Retrieve query results
records = cur.fetchall()
print(records)