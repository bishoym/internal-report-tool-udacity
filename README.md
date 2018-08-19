# Internal Reporting Tool v1 -- [report.py](report.py)

This is an internal reporting tool project created in fulfillment of Udacity's Full Stack Web Developer NanoDegree.
The aim of this project is to answer three questions in three advanced SQL queries using the PostgreSQL database system.

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
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze. This project was created using Vagrant running on Virtual Box. You will need the [`newsdata.sql`](newsdata.sql) file

## License
 The content of this repository is created by Bishoy Maher and is licensed under the [MIT License](https://opensource.org/licenses/MIT)
