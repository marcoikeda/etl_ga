#get sessions and persist in RDS instance
import pymysql as sql

con = sql.connect('mysqltest.cyzy5ereqqzd.us-east-1.rds.amazonaws.com', user, password, port=3306)