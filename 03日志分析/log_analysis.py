#!/usr/bin/env python3

import psycopg2
DBNAME = "news"
# query the most popular accessed three articles and views from news database.
articles_query = "select articles.title,count(*) as num " \
                 "from articles,log " \
                 "where log.path like '%' || articles.slug " \
                 "and log.status like '%200%' " \
                 "group by log.path,articles.title " \
                 "order by num desc " \
                 "limit 3"
# query the most popular article authors and views from news database.
authors_query = "select subquery1.name,sum(subquery1.num) as num " \
                "from (select authors.name,count(*) as num " \
                       "from articles,log ,authors " \
                       "where log.path like '%' || articles.slug " \
                       "and articles.author = authors.id " \
                       "and log.status like '%200%'" \
                       "group by log.path,authors.name) " \
                       "subquery1 " \
                "group by subquery1.name " \
                "order by num desc"
# query on which days more than 1% of requests lead to errors from news
# database.
errors_query = "select subquery1.day," \
               "round(100*(subquery2.errors::numeric / " \
               "subquery1.num::numeric)" \
               ",1) as error_rate " \
               "from (select date_trunc('day', log.time)::date as day, " \
                         "count(*) as num from log group by 1 order by 1) " \
                         "subquery1," \
               "(select date_trunc('day', log.time)::date as day, " \
                         "count(*) as errors " \
                         "from log " \
                         "where log.status = '404 NOT FOUND' " \
                         "group by 1 " \
                         "order by 1)" \
                         "subquery2 " \
               "where subquery1.day = subquery2.day and " \
               "round(100*(subquery2.errors::numeric / " \
               "subquery1.num::numeric)" \
               ",1) >= 1"
# get_pop_info make articles_query or authors_query above as input and output
# list of result.


def get_pop_info(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    out_list = []
    for item in c.fetchall():
        out_list.append("{} -- {} views.".format(item[0], item[1]))
    return out_list
    db.close()
# get_errors_rate make errors_query above as input and output list of result.


def get_errors_rate(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    out_list = []
    for item in c.fetchall():
        out_list.append("{} -- {}% errors rate.".format(item[0], item[1]))
    return out_list
    db.close()
# Creat log_report.txt file and write above queries'results by line.


with open("log_report.txt", "w", encoding="utf-8") as f:
    f.write("1.What are the most popular three articles of all time? " + '\n')
    f.write('\n'.join(get_pop_info(articles_query)) + '\n')
    f.write("2.Who are the most popular article authors of all time? " + '\n')
    f.write('\n'.join(get_pop_info(authors_query)) + '\n')
    f.write("3.On which days did more than 1% of requests lead to errors? " +
            '\n')
    f.write('\n'.join(get_errors_rate(errors_query)) + '\n')
