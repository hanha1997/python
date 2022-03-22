import psycopg2
import config


def create_table():
    cnt = create_connection()
    cursor = cnt.cursor()
    query = '''CREATE TABLE IF NOT EXISTS car (
            id SERIAL PRIMARY KEY NOT NULL,
            car_name VARCHAR(50) NOT NULL,
            license_plate VARCHAR(15) NOT NULL,
            is_checkin INT,
            deposits INT,
            time_in TIMESTAMP,
            time_out TIMESTAMP
    )'''
    cursor.execute(query)
    cnt.commit()
    cnt.close()

def create_connection():
    #mở kết nối đến postgres db
    try:
        connect = psycopg2.connect(
                host = config.localhost,
                dbname = config.database,
                user = config.username,
                password = config.password,
                port = config.port_id
            )

        return connect

    except Exception as error:
        print(error)    

