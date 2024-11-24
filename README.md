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

  * CLI: python manage.py makemigrations

  * CLI: python manage.py migrate

  * django handles the database commands

  * speaking of django, the admin site is available at localhost:8000/admin

  * this is the only place to remove books

  * to log in, first run

  * CLI: python manage.py createsuperuser

  * and follow the instructions to get the username and password

Further comments on objectives:

  1. Table has the required columns
  2. SQLite is already set up, with a few books in the table
  3. To start adding a new book, click the "Add Book" button on the home page or visit http://localhost:8000/new_book/
     * If the entered data is valid, the book entry will be added to the database
     * The data is valid if there is a name, author, and publication date, and if there is an ISBN it is valid
     * Genre and ISBN are optional
     * Filtering is done at http://localhost:8000/books/ , which is initially populated with all books
     * While the homepage is populated with only the latest published several, and with minimal details
     * http://localhost:8000/books/ can also be reached by clicking "See all books" on the homepage
     * The columns with textboxes can be filtered, and so can dates within a range
     * Write some text you want to match in the corresponding field, and optionally select start and end dates to look for publications
     * Then click "Filter"
     * The results of the filter will then be displayed in the table, where all of the books used to be
     * To clear the filters and see all books, click "Reset"
  4. To export book data, first see 3. to navigate to the right page
     * Clicking "Export book list" in the nav bar will download a csv of the filtered book list
     * Click "Reset" and then "Export book list" will get all the books in the database
     * books.csv will have a header
  5. These are reachable from the home page
     * Add Book Form: at http://localhost:8000/new_book/
     * Filter Form: at http://localhost:8000/books/
     * Books List: at http://localhost:8000/books/
     * Export Button: "Export book list" on http://localhost:8000/books/
  6. The interface is responsively design using django and bootstrap
  7. Book entry constraints:
     * entry id is auto generated to be a unique primary key
     * title is a string with max length of 100
     * author is a string with max length of 100
     * genre is a string with max length of 50
     * pub_date is a date
     * isbn is a string with max length 17
  8. CRUD:
     * create at http://localhost:8000/new_book/
     * this handles invalid inputs
     * retrieve at http://localhost:8000/books/
     * update at localhost:8000/admin
     * delete at localhost:8000/admin

Design decisions:
1. Using django makes maneuvering the database, tables, and entries easy
2. SQLite is the default database
3. Django makes web apps easy to design
4. The webpages were chosen by their purposes, mostly distinct, but for example the filtered list and all books share a space
5. ISBN was left optional because the initial example books I wanted to use wre published before the ISBN was established and thus didn't have any
6. Filtering was chosen to be inclusive as opposed to exact
7. Export was chosen to be csv
8. For CRUD operations, Update and Delete were not specified for regular users, so at the moment only admins have access
