# DAIMIL10-SQL-Case-Study

BY: Joel Encarnacion, Jasmine Hardin, Andrew Orlando, David Scott

## Setup:
Install the required libraries: pandas, psycopg2, dotenv, and argparse.
create a .env file with the following environment variables:
```
PG_DBNAME (your database name)
PG_USER (your database user)
PG_PASSWORD (your database password)
PG_HOST (your database host)
PG_PORT (your database port)
```

## HR Department README
### HR.py
This script is designed to help the HR department export employee Paid Time Off (PTO) data from the company's SQL database into an Excel file. It can also count the number of employees meeting the PTO criteria. Here’s how to use it:

    Script Execution:
        Run the script from the command line. Specify the threshold for PTO hours to filter employees. Example: python script.py 80 (filters employees with at least 80 hours of PTO).
        Count Flag: Use the -c or --count_query flag if you want the script to count and display the number of affected employees. Example: python script.py 80 -c.

    Output:
        The script will generate an Excel file (get_workaholics.xlsx) in the ../excel_reports/ directory containing the filtered PTO data.
        If the count flag is used, the script will also print the number of employees meeting the threshold criteria.

Example usage:
```python script.py 80```
```python script.py 80 -c```

## Sales Team README
### Prices.py/Prices2.py

- These script will generate an Excel file (Prices_per_subcategory.xlsx) in the ../excel_reports/ directory containing the following data for each product category and subcategory:
        category_name: Name of the product category
        subcategory_name: Name of the product subcategory
        lowest_price: Lowest price within the subcategory
        highest_price: Highest price within the subcategory
        price_difference: Difference between the highest and lowest price
        product_count: Number of products in the subcategory

- Use prices.py if you need an overview of price data by category.

- Use prices2.py if you require a more detailed analysis that includes both category and subcategory levels.

Example usage:
`python prices2.py`
