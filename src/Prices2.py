import pandas as pd
import psycopg2
import os
import argparse
from dotenv import load_dotenv

def main():
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
    SELECT
    pc.name AS category_name,
    psc.name AS subcategory_name,
    MIN(pch.standardcost) AS lowest_price,
    MAX(pch.standardcost) AS highest_price,
    MAX(pch.standardcost) - MIN(pch.standardcost) AS price_difference,
    COUNT(p.productid) AS product_count
FROM
    production.productcategory pc
JOIN
    production.productsubcategory psc ON pc.productcategoryid = psc.productcategoryid
JOIN
    production.product p ON p.productsubcategoryid = psc.productsubcategoryid
JOIN
    production.productcosthistory pch ON p.productid = pch.productid
GROUP BY
    pc.name, psc.name
ORDER BY
    pc.name, psc.name
    '''

    

    # Step 3: Execute the main SQL query and fetch results
    df = pd.read_sql_query(pto_query, conn)

    # Step 4: Ensure the output directory exists
    output_file = '../excel_reports/Prices_per_subcategory.xlsx'
    folder_path = os.path.dirname(output_file)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Step 5: Export the result to a CSV file
    df.to_excel(output_file, index=False)

    conn.close()

    print(f"Data has been exported to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export SQL query result to an Excel file.')
    
    args = parser.parse_args()
    
    main()
