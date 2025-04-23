import psycopg2

conn = psycopg2.connect(
    host="my_postgres",  # container name = DNS within Docker network
    database="mydb",
    user="admin",
    password="adminpassword",
    port=5432
)
