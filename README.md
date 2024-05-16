# JSON to MySQL Converter

This script converts JSON data into a MySQL database table. Each JSON object is inserted as a separate row in the table, with the keys in the JSON objects mapped to column names in the table.

## PHP Script

### Purpose

The purpose of the PHP script is to automate the process of inserting JSON data into a MySQL database using PHP.

### Prerequisites

- PHP installed on your system
- Access to a MySQL database
- JSON data file to be converted

### Usage

```bash
php json_to_mysql.php --file <json_file> --database <database_name> --table <table_name> [--server <server_name>] [--user <username>] [--password <password>]
```

- `--file <json_file>`: Path to the JSON file containing the data to be inserted.
- `--database <database_name>`: Name of the MySQL database where the table will be created and data will be inserted.
- `--table <table_name>`: Name of the table to be created in the database.
- `--server <server_name>` (Optional): MySQL server name. Default is 'localhost'.
- `--user <username>` (Optional): MySQL username. Default is empty.
- `--password <password>` (Optional): MySQL password. Default is empty.

### Additional Notes

- **ID Column**: An 'id' column is automatically created as the primary key for the table.
- **JSON Structure**: The JSON data should be a flat array of objects. Nested JSON structures are not supported.
- **Field Names**: Field names in the JSON objects should be consistent across all objects. Each field will become a column in the MySQL table.

### Example

```bash
php json_to_mysql.php --file data.json --database my_database --table my_table --server localhost --user my_username --password my_password
```

This command will read the data from 'data.json' and insert it into the 'my_table' table in the 'my_database' database on the MySQL server running at 'localhost', using the specified username and password.

## Python Script

### Purpose

The purpose of the Python script is to automate the process of inserting JSON data into a MySQL database using Python.

### Prerequisites

- Python installed on your system
- Access to a MySQL database
- JSON data file to be converted

### Usage

```bash
python json_to_mysql.py --file <json_file> --database <database_name> --table <table_name> [--server <server_name>] [--user <username>] [--password <password>]
```

- `--file <json_file>`: Path to the JSON file containing the data to be inserted.
- `--database <database_name>`: Name of the MySQL database where the table will be created and data will be inserted.
- `--table <table_name>`: Name of the table to be created in the database.
- `--server <server_name>` (Optional): MySQL server name. Default is 'localhost'.
- `--user <username>` (Optional): MySQL username. Default is empty.
- `--password <password>` (Optional): MySQL password. Default is empty.

### Additional Notes

- **ID Column**: An 'id' column is automatically created as the primary key for the table.
- **JSON Structure**: The JSON data should be a flat array of objects. Nested JSON structures are not supported.
- **Field Names**: Field names in the JSON objects should be consistent across all objects. Each field will become a column in the MySQL table.

### Example

```bash
python json_to_mysql.py --file data.json --database my_database --table my_table --server localhost --user my_username --password my_password
```

This command will read the data from 'data.json' and insert it into the 'my_table' table in the 'my_database' database on the MySQL server running at 'localhost', using the specified username and password.
```

Feel free to use and modify this README.md for your project! Let me know if you need any further assistance.
