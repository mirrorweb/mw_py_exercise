The following requirements should be fulfilled, where possible, though they should not be considered restrictions.

If a candidate wishes to expand upon or alter these steps in a way that does not negatively affect the end result - that
is perfectly acceptable but please leave comments to explain why you have done so.

If a candidate is unable to fulfill a requirement, move on to the next one and complete as many as possible.


# 1.0 Environment
Create a virtual environment for the project and install the following dependancies:
- python 3.7 (or higher)
- pymysql
- quart

# 1.1 Database
Set up a local MYSQL database with two tables:
- company
- employee
See [mw_py_exercise/database/README](mw_py_exercise/database/README.mb) for further instructions.

# 1.2 Project Foundation
Build a simple web application using Quart (the async version of the Flask framework).
Add three routes:
- index
- company
- employee
Create a HTML template file for each route.
Use Bootstrap 4 for styling.

# 1.3 MYSQL client
Establish a pymysql client to interact with the database.
Use a .env file to store the database connection details (host, username, password).

# 2.0 Data Processing
Write a python function to ingest the JSON file from the data folder.
Process the raw data to match the expected record structures.
Insert this data into the database.

# 2.1 SQL Queries
Write SQL code to interact with database records, to be used in the app routes.
This includes insert, update & delete logic for each table.

# 3.0 Routes
Create Quart routes for displaying and editing records.
See [mw_py_exercise/routes/README](mw_py_exercise/routes/README.mb) for further instructions.

# 3.1 Adding records
Add a method of adding company and employee records in the app.

# 3.2 Deleting records
Add a method of deleting company and employee records in the app.

# 4.0 Error handling
Ensure that all code has adequate error handling.

# 4.1 logging
Add logging to the project to output relevant information to the console.

# 5.0 Unit testing
Add a basic unit test suite with a few good examples of how to test a web application.
See [tests/README](tests/README.mb) for further instructions.

# 1.4 Requirements
Please generate a requirements txt file for this project.

# 1.5 Instructions
[write step-by-step instructions here on how to replicate the setup of this apllication on another machine]

# 6.0 Pull Request
Commit & push code changes to the branch and open a pull request against the main branch.

# 7.0 Additional task
Imagine that MirrorWeb puts forward a requirement for a second web application to be built which will act as a company
portal where employees can log in and have a read-only view of the database records for the company that they belong to.

Leave a comment on your pull request describing how you might go about converting the backend of this project into an 
API, what kind of structure it would have & what benefits this may provide.

