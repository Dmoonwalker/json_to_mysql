import json
import mysql.connector
import argparse

def insert_json_data(json_file, server, database, table, user='', password=''):
    # Validate JSON file
    try:
        with open(json_file) as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print("Error: JSON file does not exist.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return

    # Validate database and table names
    if not database or not table:
        print("Error: Database and table names must be provided.")
        return

    # Handle null username and password
    user = user or ''
    password = password or ''

    try:
        # Create MySQL connection
        connection = mysql.connector.connect(
            host=server,
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error as err:
        print("Error: Failed to connect to MySQL database:", err)
        return

    try:
        # Create MySQL cursor
        cursor = connection.cursor()

        # Create table if not exists
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} (id INT AUTO_INCREMENT PRIMARY KEY, data JSON)")

        # Insert JSON data into MySQL table
        for item in json_data:
            cursor.execute(f"INSERT INTO {table} (data) VALUES (%s)", (json.dumps(item),))
            print("Data inserted successfully:", cursor.lastrowid)

        # Commit changes
        connection.commit()

    except mysql.connector.Error as err:
        print("Error: MySQL error occurred:", err)
        connection.rollback()

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

# Parse command line arguments
parser = argparse.ArgumentParser(description="Convert JSON data to MySQL database entries")
parser.add_argument("json_file", help="Path to the JSON file")
parser.add_argument("--server", help="MySQL server (default: localhost)", default="localhost")
parser.add_argument("--database", help="MySQL database name", required=True)
parser.add_argument("--table", help="MySQL table name", required=True)
parser.add_argument("--user", help="MySQL username", default="")
parser.add_argument("--password", help="MySQL password", default="")
args = parser.parse_args()

# Example usage
insert_json_data(args.json_file, args.server, args.database, args.table, args.user, args.password)
