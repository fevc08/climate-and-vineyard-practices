import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=LAPTOP-7SGK046V;'
        'DATABASE=your_database_name;'
        'Trusted_Connection=yes;'
    )
    return conn

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    conn.close()