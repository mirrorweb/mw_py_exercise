import pymysql
from settings import LOCAL_HOST, USER, PASSWORD, DATABASE


async def connection():
    # Connect to the database
    conn = pymysql.connect(host=LOCAL_HOST,
                           user=USER,
                           password=PASSWORD,
                           database=DATABASE,
                           cursorclass=pymysql.cursors.DictCursor)
    return conn
