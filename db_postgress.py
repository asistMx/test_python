import psycopg2

def connection():
    
    try:
        connection = psycopg2.connect(  
                                        user="postgres",
                                        password="Pap315a",
                                        host="localhost",
                                        port="5432",
                                        database="test_db"
                                    )
        return connection
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        return None
    

def read(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test_table")
    record = cursor.fetchall()
    print("Result ", record)
    cursor.close()
    return record