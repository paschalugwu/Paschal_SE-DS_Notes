#!/bin/bash

# Install python3.8-venv
sudo apt-get install python3.8-venv -y

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install necessary packages
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev -y

# Install Python packages
pip3 install mysqlclient SQLAlchemy

# Update the system
sudo apt-get update

# Install and start mysql server
sudo apt-get install mysql-server -y
sudo service mysql start

# Check the status of mysql
sudo service mysql status

# Run the Python script
python3 << EOF
from sqlalchemy import create_engine, text

# MySQL connection parameters
user = 'root'            # MySQL username
password = 'benziopax'   # MySQL password
host = 'localhost'       # MySQL host

# Construct the connection string
connection_string = f"mysql://{user}:{password}@{host}"

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Establish a connection
connection = engine.connect()

# Execute a raw SQL query to retrieve the list of databases
query = text("SHOW DATABASES;")
result = connection.execute(query)

# Fetch the list of databases from the result
databases = [row[0] for row in result.fetchall()]

# Print the list of databases
print("List of databases:")
for db in databases:
    print(db)

# Close the connection
connection.close()
EOF
