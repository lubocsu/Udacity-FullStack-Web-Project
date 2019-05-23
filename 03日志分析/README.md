# **log analysis reporting tool** #
----------
## Introduction ##
log_analysis is an internal reporting tool that will use information from the log database to generate a report on answers about the site's user activity.
## To do list##
- report most popular three articles.
- report most popular article authors.
- report date of more than 1% of requests lead to errors.
## Requirements ##
- VirtualBox(5.1+)
- Vagrant(1.9.1+)
- Python(3.2+)
- Python psycopg2 module
- Unix shell(Mac or Linux system)
- Git bash（Windows system）
- PostgreSQL
##Get necessary file##
- [VM configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
- [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
##Quick start##
1. From your terminal, inside the vagrant subdirectory, run the command `vagrant up`.
2. When `vagrant up` is finished running,you can run `vagrant ssh` to log in.
3. Then you can run `cd /vagrant`To access your shared files.
4. run the command `python3 log_analysis.py` to run this tool.

**notice:** Put newsdata.sql and log_analysis.py file into the vagrant directory, which is shared with your virtual machine.
