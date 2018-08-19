# Internal Reporting Tool v1.0 -- [report.py](report.py) -- 19/08/2018

This is an internal reporting tool project created in fulfillment of Udacity's Full Stack Web Developer NanoDegree.
The aim of this project is to answer three questions in three advanced SQL queries using the PostgreSQL database system.

## Dependencies
- Python 2.7.12 or higher (Download [here](https://www.python.org/downloads/))
- VirtualBox  5.1.38 r122592 (Qt5.6.2) (Download [here](https://www.virtualbox.org/wiki/Downloads))
- Vagrant 2.1.2 (Download [here](https://www.vagrantup.com/downloads.html))
- PostgreSQL 9.5.13 (Download [here](https://www.postgresql.org/download/))
- [News Database File](newsdata.sql)

## Contents
The database included by the project providers [`newsdata.sql`](newsdata.sql) contains 3 tables: **Authors, Articles, & Log**

 The questions answered by this program are:
1. "What are the most popular three articles of all time?"
2. "Who are our most popular article authors of all time?"
3. "On which days did more than 1% of requests lead to errors?"

## My Approach
- For Task 1, a subquery was used to create a new version of the log table with the paths translated to slugs. This new column was used as the basis for a join. The views were totaled based on a count of all the times a valid slug (matched with articles table) was visited, regardless of whether or not that was a hit or miss.
- For Task 2, the same query was used with the addition of a join to the authors table in order to display the most viewed authors. _(Note: a view would have simplified the query)._
- For Task 3, I ran three queries within one another. The first was to create a table of the date | total requests | errors. The second carried out the arithmetic necessary to calculate the percentages leaving a table of date | percent. The final query limited the results to only those that exceeded 1% as per the requirement. Not the most eloquent bit of code, but it gets the job done.

## Take the Challenge
To start on this project, you'll need to download and install all the dependencies mentioned above. You need the database software (provided by a Linux virtual machine) and the data to analyze. This project was created using Vagrant running on Virtual Box. Check the following Setup section for more details on how to get up and running. You will also need the [`newsdata.sql`](newsdata.sql) file

## Setup/Installation
- Once you have vagrant setup on VirtualBox you can use your terminal to start the VM using `vagrant up` _(Note: this will take a while the first time you launch as vagrant is downloading extra dependencies)_
- Follow that with `vagrant ssh` to log into your VM _(Note: On some Windows systems, you will need to use `winpty vagrant ssh` instead of `vagrant ssh`)_

_(Note: You may check everything is working by using the commands `python` and `psql` to make sure you have installed both correctly)_

- Once inside your VM you can explore the database with `psql -d news` which will connect you to the database _(Note: You can use \dt to list all the tables, \d <tablename> to explore specific tables, \q to exit)_
- Run the file using the command `python report.py`

## Usage
This program can easily run from the command line using: `python report.py`
If you're using python 3 you may need to use `python3 report.py`

## License
 The content of this repository is created by Bishoy Maher and is licensed under the [MIT License](LICENSE.md)
