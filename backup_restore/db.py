import psycopg2


class DbPostgres:
    def __init__(self, host, port, dbname, user, password) -> None:
        self.host = host
        self.dbname = dbname
        self.port = port
        self.user = user
        self.password = password
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print(f"DB connection successful!! Connected at {self.dbname}")
        except Exception as e:
            print("Error in postgres connection",e)

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result

        except psycopg2.Error as e:
            print("Error executing query:", e)
            return None
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed.")