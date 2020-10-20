import requests
from datetime import datetime as dt
import time
import psycopg2


def getconnection(user=None,password=None,host=None,database=None):
    con = None
    try:
        con = psycopg2.connect(host=host,database=database,user = user,password = password)
    except (Exception, psycopg2.Error) as error :
        print ("Error Connecting : ", error)
    return con


try:
    con = getconnection(user="allsafe",database="AllSafeP1",password = "123456",host="localhost")
    cursor = con.cursor()
    print (con.get_dsn_parameters())
    SQL = "Insert into allsafe (datetime,statuscode) values (%s,%s)"
    print("MetrixGenerator  Started : \n")
    print("TimeStamp  \t\t Status Code")
    while True:
        response = requests.get('https://allsafe.in/')
        timenow = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(SQL,(timenow,response.status_code))
        con.commit()
        print(timenow+" \t "+str(response.status_code))
        time.sleep(0.500)
except (Exception, psycopg2.Error) as error :
    print ("Error : ", error)
finally:
        if(con):
            cursor.close()
            con.close()
            print("Connection Closed")