import pandas as pd
import db

def export_data():
    cnt = db.create_connection()
    sql_query = pd.read_sql_query('''
                                select *, SUM(deposits) from car
                                '''
                                , cnt) 

    df = pd.DataFrame(sql_query)
    df.to_csv (r'C:\Users\hanhm\Downloads\exported_data.csv', index = False) 