import os
from dotenv import load_dotenv
import mysql.connector


load_dotenv()

MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_USER = os.environ["MYSQL_USER"] 
MYSQL_PW = os.environ["MYSQL_PW"]



def create_mysql_connection(scaling_factor):

    if scaling_factor == 0.01:
        database = "tpc-h_small"
    if scaling_factor == 0.1:
        database = "tpc-h_medium"
    if scaling_factor == 1:
        database = "tpc-h_large"

    mysql_conncetion = mysql.connector.connect(user = MYSQL_USER, password = MYSQL_PW, host = MYSQL_HOST, database = database)

    return mysql_conncetion