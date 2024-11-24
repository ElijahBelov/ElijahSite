See objectives.txt

Usage:

Download files 

  * Either with github website or git clone CLI

Have python

Have Django

  * CLI: pip install django

Start server:

  * cd to folder containing manage.py then

  * CLI: python manage.py runserver 8000
  
  * note: 8000 is a semi-arbitrary port

Check it out:

  * open browser
  
  * browse to localhost:8000/

Notes:

  * database used is SQLite

  * database is already setup

  * but if you want to make changes to the tables or record details

  * use the usual django commands
    
  *   CLI:

  * python manage.py makemigrations

  * python manage.py migrate

  * django handles the database commands
