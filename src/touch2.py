import pandas as pd
import psycopg2
import os
import argparse
from dotenv import load_dotenv

def main(threshold, count_query):
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

    # Step 2: Construct the SQL query
    pto_query = f'''
    SELECT person.firstname as first_name,
           person.lastname as last_name,
           employee.vacationhours as pto
    FROM person.person
    JOIN humanresources.employee
        ON person.businessentityid = humanresources.employee.businessentityid
    WHERE employee.vacationhours >= {threshold}
    GROUP BY person.businessentityid, employee.vacationhours
    '''

    if count_query:
        count_query_str = f'''
        SELECT COUNT(*) AS affected_employees
        FROM (
        {pto_query}
        ) AS subquery;
        '''
        cur = conn.cursor()
        cur.execute(count_query_str)
        cnt_result = cur.fetchone()
        print(f"Number of affected workaholics: {cnt_result[0]}")

    # Step 3: Execute the main SQL query and fetch results
    df = pd.read_sql_query(pto_query, conn)

    # Step 4: Ensure the output directory exists
    output_file = '../excel_reports/get_workaholics.csv'
    folder_path = os.path.dirname(output_file)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Step 5: Export the result to a CSV file
    df.to_csv(output_file, index=False)

    conn.close()

    print(f"Data has been exported to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export SQL query result to an Excel file.')
    parser.add_argument('threshold', type=int, help='Threshold for PTO hours')
    parser.add_argument('-c', '--count_query', action='store_true', help='Flag to count affected employees')

    args = parser.parse_args()
    
    main(args.threshold, args.count_query)
