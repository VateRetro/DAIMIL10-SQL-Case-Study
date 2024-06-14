import pandas as pd
import psycopg2
import os
import argparse
from dotenv import load_dotenv

def main(threshold):
    load_dotenv()

    DBNAME = os.getenv('PG_DBNAME')
    USER = os.getenv('PG_USER')
    PASSWORD = os.getenv('PG_PASSWORD')
    HOST = os.getenv('PG_HOST')
    PORT = os.getenv('PG_PORT')

    # Step 1: Connect to your SQL database
    conn = psycopg2.connect(dbname=DBNAME,
                            user=USER,
                            password=PASSWORD,
                            host=HOST,
                            port=PORT)

    # Step 2: Construct and execute the SQL query
    pto_query = f'''
    SELECT person.firstname as first_name,
           person.lastname as last_name,
           employee.vacationhours as pto
    FROM person.person
    JOIN humanresources.employee 
        ON person.businessentityid = humanresources.employee.businessentityid
    WHERE employee.vacationhours >= {threshold}
    GROUP BY person.businessentityid, employee.vacationhours
    LIMIT 10;
    '''
    df = pd.read_sql_query(pto_query, conn)

    # Step 3: Ensure the output directory exists
    folder_path = os.path.dirname('../sql_queries/get_workaholics.xlsx')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Step 4: Export the result to an Excel file
    df.to_excel('../sql_queries/get_workaholics.xlsx', index=False)

    conn.close()

    print(f"Data has been exported to {folder_path}/get_workaholics.xlsx")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export SQL query result to an Excel file.')
    parser.add_argument('threshold', type=int, help='Threshold for PTO hours')

    args = parser.parse_args()
    
    main(args.threshold)
