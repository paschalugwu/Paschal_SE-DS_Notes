# AirBnB clone (MySQL) - Bug Free!

## Introduction

In this section, we will focus on ensuring that our AirBnB clone project is free from bugs. The key to achieving this is through the use of the `unittest` module. `unittest` is a Python testing framework that allows us to write and execute test cases for our code. In our project, we aim to cover various functionalities with test cases to ensure the overall stability and correctness of the codebase.

### Running Tests

Before we dive into writing tests, let's understand how to run them. Open your terminal and use the following commands:

```bash
# Run all tests
guillaume@ubuntu:~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$
```

This command discovers and runs all the tests in the `tests` directory. The "OK" message indicates that all the tests passed successfully.

### Database Setup

For testing with MySQL, we need to create a specific database for it. Ensure you have the necessary credentials for MySQL (user, password, host, and database name). You can set the environment variables accordingly:

```bash
export HBNB_ENV=test
export HBNB_MYSQL_USER=hbnb_test
export HBNB_MYSQL_PWD=hbnb_test_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_test_db
export HBNB_TYPE_STORAGE=db
```

### Writing Tests

Now, let's write tests to ensure that our code works as expected. Each test should follow the principle of "Assert a current state, perform an action, and validate the change in state."

For example, let's say we want to test the `create` command for creating a State named "California" in the console. Here are the steps for our unittest:

1. Get the number of current records in the `states` table using MySQLdb.
2. Execute the console command to create a new State.
3. Get the number of records in the `states` table again.
4. Check if the difference is +1; if yes, the test has passed.

```python
import unittest
import MySQLdb
from models import storage

class TestCreateState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to the MySQL database
        cls.db = MySQLdb.connect(
            host=storage._DBStorage__engine._host,
            user=storage._DBStorage__engine._user,
            passwd=storage._DBStorage__engine._pwd,
            db=storage._DBStorage__engine._db
        )
        # Create a cursor
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.db.close()

    def test_create_state(self):
        # Get the initial count of states
        initial_count = self.get_states_count()

        # Execute the console command to create a State
        # Note: Replace this with the actual console command
        # e.g., storage.create('State', name='California')

        # Get the count of states after execution
        updated_count = self.get_states_count()

        # Check if the count increased by 1
        self.assertEqual(updated_count, initial_count + 1)

    def get_states_count(self):
        # Query to get the count of states
        query = "SELECT COUNT(*) FROM states"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count

if __name__ == '__main__':
    unittest.main()
```

This test class sets up a connection to the MySQL database, defines a test case for creating a State, and checks if the count of states increases after the execution of the console command.

Remember to replace the console command with the actual command you want to test. Also, ensure that your test cases cover various functionalities, and the number of tests increases over time.

Now you can run the tests using the following command:

```bash
guillaume@ubuntu:~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$
```

This ensures that all your unittests pass without any errors, confirming the bug-free nature of your AirBnB clone project.

Remember, maintaining bug-free code and adhering to PEP8 standards are crucial for a successful project. Always run tests with each storage engine and write new tests when needed.

# AirBnB clone (MySQL) - MySQL Setup Development

## Overview

In this section, we will create a script that prepares a MySQL server for the AirBnB clone project. The script will perform the following tasks:

1. Create a database named `hbnb_dev_db`.
2. Create a new user named `hbnb_dev` on localhost.
3. Set the password of `hbnb_dev` to `hbnb_dev_pwd`.
4. Grant `hbnb_dev` all privileges on the `hbnb_dev_db` database (and only this database).
5. Grant `hbnb_dev` SELECT privilege on the `performance_schema` database (and only this database).
6. Ensure that if the database `hbnb_dev_db` or the user `hbnb_dev` already exists, the script should not fail.

## MySQL Setup Script

Create a file named `setup_mysql_dev.sql` with the following content:

```sql
-- Check if the hbnb_dev_db database already exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or update the user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user on the specified databases
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Display the list of databases to verify the setup
SHOW DATABASES;
```

## Running the Setup Script

Execute the script using the following command:

```bash
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
```

You will be prompted to enter the password for the root user.

## Verification

After running the script, you can verify the setup by checking the created database and user privileges. Use the following commands:

```bash
echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
```

You should see the `hbnb_dev_db` in the list of databases and the granted privileges for the user `hbnb_dev`.

## Conclusion

This script ensures the proper setup of a MySQL server for the AirBnB clone project. It creates the necessary database, user, and grants the required privileges. Running this script will help in establishing a MySQL environment tailored for the development needs of the project.

# AirBnB clone (MySQL) - MySQL Setup Test

In this section, we will focus on setting up the MySQL server for the testing environment of our AirBnB clone project. This script is crucial for ensuring that the necessary databases and users are in place for testing purposes.

## Script Overview

Let's break down the script step by step:

```sql
-- create project testing database with the name `hbnb_test_db`
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creating a new user named `hbnb_test` with all privileges on the db hbnb_test_db
-- with the password `hbnb_test_pwd` if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- granting the SELECT privilege for the test user hbnb_test on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- granting all privileges to the new user hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- flush privileges to apply the changes
FLUSH PRIVILEGES;
```

## Explanation

1. **Create Database:**
   ```sql
   CREATE DATABASE IF NOT EXISTS hbnb_test_db;
   ```
   - This statement creates the testing database `hbnb_test_db` if it doesn't already exist.

2. **Create User:**
   ```sql
   CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
   ```
   - This creates a new user named `hbnb_test` with the password `hbnb_test_pwd` if the user doesn't exist.

3. **Grant SELECT Privilege:**
   ```sql
   GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
   ```
   - Grants the SELECT privilege to the user `hbnb_test` on the `performance_schema` database.

4. **Grant All Privileges:**
   ```sql
   GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
   ```
   - Provides all privileges to the user `hbnb_test` specifically on the `hbnb_test_db`.

5. **Flush Privileges:**
   ```sql
   FLUSH PRIVILEGES;
   ```
   - This command reloads the privileges, applying the changes made in the script.

## Running the Script

To execute this script, use the following command in your MySQL shell:

```bash
cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
```

This will prompt you for the MySQL root password.

## Verification

After running the script, you can verify its success by checking if the database and user were created and if the necessary privileges were granted. Use the following commands:

```bash
echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
```

These commands should display the `hbnb_test_db` in the list of databases and show the granted privileges for the `hbnb_test` user.

This script ensures that the MySQL server is properly configured for testing the AirBnB clone project, allowing seamless interaction with the database during the testing phase.

# AirBnB clone (MySQL) - DBStorage: States and Cities

In this section, we will integrate SQLAlchemy into our AirBnB clone project, focusing on the transition from FileStorage to DBStorage. This change involves updating the BaseModel, City, and State classes, as well as creating a new DBStorage engine.

## Update BaseModel: (models/base_model.py)

```python
# Import SQLAlchemy's declarative_base
from sqlalchemy.ext.declarative import declarative_base

# Create Base as declarative_base
Base = declarative_base()

# Update BaseModel class
class BaseModel:
    # Existing code...

    # Add class attributes
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    # Move models.storage.new(self) to def save(self) and call it before models.storage.save()
    def save(self):
        models.storage.new(self)
        models.storage.save()

    # Update __init__ to manage kwargs and create instance attributes
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.utcnow()

    # Update to_dict method to remove '_sa_instance_state'
    def to_dict(self):
        new_dict = self.__dict__.copy()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    # Add delete method to delete the current instance from storage
    def delete(self):
        models.storage.delete(self)
```

This section includes several updates to the `BaseModel` class, integrating SQLAlchemy. Here are the key points:

- **Import declarative_base:** SQLAlchemy's `declarative_base` is imported to create the base class for our models.

- **Class attributes for BaseModel:**
  - `id`, `created_at`, and `updated_at` are now defined as class attributes using SQLAlchemy's `Column`.
  - `id` is the primary key, a unique string with a maximum length of 60 characters.
  - `created_at` and `updated_at` are datetime columns with default values set to the current UTC time.

- **Move `models.storage.new(self)` to `def save(self):`**
  - The `save` method now includes the creation of a new instance before saving it to storage.

- **Update `__init__`:**
  - The `__init__` method now handles keyword arguments to create instance attributes based on the dictionary.
  - If the 'id' is not present in the arguments, a new UUID is generated.
  - `created_at` and `updated_at` are set to the current time if not provided.

- **Update `to_dict`:**
  - Removed the '_sa_instance_state' key from the dictionary returned by `to_dict`.

- **Add `delete` method:**
  - A new public instance method `delete(self)` is introduced to delete the current instance from storage.

## Update City: (models/city.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

# Update City class
class City(BaseModel, Base):
    __tablename__ = 'cities'

    # Existing code...

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
```

This section focuses on updating the `City` class to work with SQLAlchemy:

- **Import necessary modules:** Import required modules such as `BaseModel` and `Base` from `models.base_model`, and SQLAlchemy's `Column` and `ForeignKey`.

- **Class attributes for City:**
  - `__tablename__`: Specifies the table name as 'cities'.
  - `name` and `state_id` are columns for city name and the foreign key to the 'states' table, respectively.

## Update State: (models/state.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# Update State class
class State(BaseModel, Base):
    __tablename__ = 'states'

    # Existing code...

    name = Column(String(128), nullable=False)

    # For DBStorage, add cities attribute to represent the relationship
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
```

This section updates the `State` class to accommodate SQLAlchemy:

- **Import necessary modules:** Similar to the City class, import required modules.

- **Class attributes for State:**
  - `__tablename__`: Specifies the table name as 'states'.
  - `name` is a column for the state name.
  - For `DBStorage`, a relationship `cities` is added, representing the connection with the `City` class. Cascade is set to 'all, delete' to ensure deleting a state deletes associated cities.

## New engine DBStorage: (models/engine/db_storage.py)

```python
# Import necessary modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base

# Define DBStorage class
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        # Create the engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        # Drop all tables if HBNB_ENV is 'test'
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        # Existing code...

    def new(self, obj):
        # Existing code...

    def save(self):
        # Existing code...

    def delete(self, obj=None):
        # Existing code...

    def reload(self):
        # Existing code...
```

This section introduces the `DBStorage` class, representing the database storage engine:

- **Private class attributes:**
  - `__engine` and `__session` are set to `None`.

- **Public instance methods:**
  - `__init__(self)`: Initializes the engine, linking it to the MySQL database. It uses environment variables for configuration. Tables are dropped if the environment is 'test'.
  - `all(self, cls=None)`: Queries objects from the current database session based on the class name.
  - `new(self, obj)`: Adds the object to the current database session.
  - `save(self)`: Commits all changes of the current database session.
  - `delete(self, obj=None)`: Deletes the object from the current database session.
  - `reload(self)`: Creates all tables in the database and creates the current database session.

## Update __init__.py: (models/__init__.py)

```python
# Import necessary modules
from os import getenv

# Existing code...

# Add a conditional to switch between DBStorage and FileStorage
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage instance
storage.reload()
```

This section updates the initialization of the storage instance based on the value of `HBNB_TYPE_STORAGE`:

- **Conditional import:**
  - If `HBNB_TYPE_STORAGE` is 'db', import `DBStorage` and create an instance. If not, import `FileStorage`.
  - The storage instance is reloaded after instantiation.

## State Creation:

```bash
echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

## City Creation:

```bash
echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

The final part demonstrates how to create states and cities using the new database storage engine. Commands for creating instances and verifying entries in the database are provided.

## Verification:

```bash
echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
```

```bash
echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
```

These changes incorporate SQLAlchemy into our AirBnB clone project, providing a smooth transition from FileStorage to DBStorage. It introduces the necessary attributes and relationships for States and Cities, ensuring proper database management. The creation and verification steps demonstrate the functionality of the new storage engine.

# AirBnB clone (MySQL) - DBStorage: User

In this section, we will incorporate user-related functionalities into our AirBnB clone project, specifically focusing on the User model. Follow the steps below to update the `User` class and explore the integration of these changes.

## Update User: (models/user.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

# Update User class
class User(BaseModel, Base):
    __tablename__ = 'users'

    # Existing code...

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
```

### Example Usage:

1. Create a new User:

```bash
echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

2. View all Users:

```bash
echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

3. Verify in the Database:

```bash
echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
```

These updates ensure the User model aligns with the DBStorage changes, including the addition of attributes such as email, password, first_name, and last_name. Apply these modifications to enhance the user-related functionalities in your AirBnB clone project.

# AirBnB clone (MySQL) - DBStorage: Place, User, City

In this section, we will extend our AirBnB clone project to handle Places, Users, and Cities more effectively with the integration of DBStorage. Follow the steps below to update the respective classes and understand the changes made.

## Update Place: (models/place.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

# Update Place class
class Place(BaseModel, Base):
    __tablename__ = 'places'

    # Existing code...

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
```

## Update User: (models/user.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# Update User class
class User(BaseModel, Base):
    __tablename__ = 'users'

    # Existing code...

    places = relationship('Place', cascade='all, delete', backref='user')
```

## Update City: (models/city.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# Update City class
class City(BaseModel, Base):
    __tablename__ = 'cities'

    # Existing code...

    places = relationship('Place', cascade='all, delete', backref='city')
```

### Example Usage:

1. Create a new Place:

```bash
echo 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

2. View all Places:

```bash
echo 'all Place' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

3. Verify in the Database:

```bash
echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
```

These updates enhance the relationships between Places, Users, and Cities in your AirBnB clone project. The changes include foreign key connections, relationships, and cascading deletions to ensure data integrity.

# AirBnB clone (MySQL) - DBStorage: Review, User, Place

In this section, we will enhance our AirBnB clone project by introducing Reviews and managing relationships between Reviews, Users, and Places using DBStorage. Follow the steps below to apply these changes effectively.

## Update Review: (models/review.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

# Update Review class
class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    # Existing code...

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
```

## Update User: (models/user.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# Update User class
class User(BaseModel, Base):
    __tablename__ = 'users'

    # Existing code...

    reviews = relationship('Review', cascade='all, delete', backref='user')
```

## Update Place: (models/place.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# Update Place class
class Place(BaseModel, Base):
    __tablename__ = 'places'

    # Existing code...

    reviews = relationship('Review', cascade='all, delete', backref='place')
```

### Example Usage:

1. Create a new User and Review:

```bash
echo 'create User email="bob@hbtn.io" password="bobpwd" first_name="Bob" last_name="Dylan"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

```bash
echo 'create Review place_id="ed72aa02-3286-4891-acbc-9d9fc80a1103" user_id="d93638d9-8233-4124-8f4e-17786592908b" text="Amazing_place,_huge_kitchen"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

2. View all Reviews:

```bash
echo 'all Review' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

3. Verify in the Database:

```bash
echo 'SELECT * FROM reviews\G' | mysql -uhbnb_dev -p hbnb_dev_db
```

These updates introduce Reviews to your AirBnB clone project and establish relationships with Users and Places. The changes include foreign key connections, relationships, and cascading deletions for data integrity.

# AirBnB clone (MySQL) - DBStorage: Amenity... and BOOM!

In this section, we will enhance our AirBnB clone project by introducing Amenities and creating a Many-to-Many relationship between Places and Amenities using DBStorage. Follow the steps below to apply these changes effectively.

## Update Amenity: (models/amenity.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

# Update Amenity class
class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    # Existing code...

    name = Column(String(128), nullable=False)
```

## Update Place: (models/place.py)

```python
# Import necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

# Define place_amenity Table
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

# Update Place class
class Place(BaseModel, Base):
    __tablename__ = 'places'

    # Existing code...

    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)
```

### Example Usage:

Create a Python script (e.g., main_place_amenities.py) to test the Many-to-Many relationship:

```python
#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *

# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")
```

Run the script:

```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./main_place_amenities.py
```

Verify the data in the database:

```bash
echo 'SELECT * FROM amenities\G' | mysql -uhbnb_dev -p hbnb_dev_db
echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
echo 'SELECT * FROM place_amenity\G' | mysql -uhbnb_dev -p hbnb_dev_db
```

These updates introduce Amenities to your AirBnB clone project and establish a Many-to-Many relationship with Places using a linking table (place_amenity). The example script demonstrates how to create, link, and save data with these new features.
