# GCG Trust test exercise
Just a GCG Trust test exercise

## Explanation
```
Task:

PART I: INTRO
1. Create new Django app. Deploy it on the server with WSGI (Apache2). Take ServerName from 'server.txt'
2. Upload the database 'data.sql' to server. Connect your Django App to it. Install software on the server if required.

PART II: APP
1. Create Model of the Database.
2. Create an interface (view) for user which will contain:
Table with 100 records per page, with pagination. Columns are:
-event_time
-client_name (if empty f'{first_name} {last_name}', if also empty 'N/A')
-action
-amount (0 if nothing)
-currency
-country
-affiliateId

3. Create filters:
1) -When you click 'affiliateId' in table display all records of this affiliateId
   -Select option 'action' and filter by it (loop all possible cases)	
   -List of counties with checkboxes - check possible countries and press 'apply' button to display records of corresponding countries

2) -Date range filter - pick two dates and get records beetwen them
   -Create date range shortcuts:
	1) Today
	2) Yesterday
	3) Last Week
	4) Last Month
	5) Last Year

Good luck!
```

## Setup
For run the project you need to install requirements from [requirements.txt](requirements.txt) file and run the following command 
```
python manage.py runserver
```

## Configuration

The following environment variables are *required*:

| Name              | Purpose                                          |
|-------------------|--------------------------------------------------|
| `DB_DRIVER`       | Engine for connecting to db.                     |
| `DB_NAME`         | The database name.                               |
| `DB_USER`         | The database user.                               |
| `DB_PASS`         | The database password.                           |
| `DB_HOST`         | The hostname of a database server.               |
| `DB_PORT`         | The port of a database server.                   |
